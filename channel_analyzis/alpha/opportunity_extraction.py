import os
from extraction_schemas import OpportunitySchema
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import uuid
from typing import List, TypedDict
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import json
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    ToolMessage,
)
from pydantic import BaseModel
from enum import Enum

load_dotenv()
MESSAGES_PATH="./test.json"
EXAMPLES_PATH="./examples.json"
RESULTS_PATH="./results.json"
MODEL_NAME="llama-3.1-70b-versatile"
TEMPERATURE=0.5
MAX_RETRIES=4
BASE_PROMPT="You are an expert extraction algorithm. Your task is to extract only the relevant information " \
            "from the provided text. For each attribute, extract the value based on the information available " \
            "in the text. If an attribute's value is not explicitly mentioned or cannot be determined, return " \
            "null or empty list (depends on attribut description). Ensure all dates and times are formatted as dd.mm.yy hh:mm and that " \
            "extracted information is written in **perfect Ukrainian** without any spelling or grammatical errors. " \
            "Proper names, such as names of people, organizations, and locations, should be extracted as-is and not translated. " \
            "Only provide the requested fields."


class Opportunity:
    pass


class ExtractionStatus(Enum):
    SUCCESS = "Success"
    FAIL = "Fail"


class ExtractionResponse:    
    status: ExtractionStatus
    response: OpportunitySchema = None
    error_message: str = None
    
    def to_json(self):
        outcome_dict = {
            "status": self.status.value,
        }
        if self.response is not None:       
            outcome_dict["response"] = self.response.__dict__
        if self.error_message is not None:
            outcome_dict["error_message"] = self.error_message
            
        return outcome_dict


llm = ChatGroq(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    max_retries=MAX_RETRIES,
    disable_streaming=True,
)


class Example(TypedDict):
    """A representation of an example consisting of text input and expected tool calls.

    For extraction, the tool calls are represented as instances of pydantic model.
    """

    input: str  # This is the example text
    tool_calls: List[BaseModel]  # Instances of pydantic model that should be extracted


def tool_example_to_messages(example: Example) -> List[BaseMessage]:
    """Convert an example into a list of messages that can be fed into an LLM.

    This code is an adapter that converts our example to a list of messages
    that can be fed into a chat model.

    The list of messages per example corresponds to:

    1) HumanMessage: contains the content from which content should be extracted.
    2) AIMessage: contains the extracted information from the model
    3) ToolMessage: contains confirmation to the model that the model requested a tool correctly.

    The ToolMessage is required because some of the chat models are hyper-optimized for agents
    rather than for an extraction use case.
    """
    messages: List[BaseMessage] = [HumanMessage(content=example["input"])]
    openai_tool_calls = []
    for tool_call in example["tool_calls"]:
        openai_tool_calls.append(
            {
                "id": str(uuid.uuid4()),
                "type": "function",
                "function": {
                    # The name of the function right now corresponds
                    # to the name of the pydantic model
                    # This is implicit in the API right now,
                    # and will be improved over time.
                    "name": tool_call.__class__.__name__,
                    "arguments": tool_call.json(),
                },
            }
        )
    messages.append(
        AIMessage(content="", additional_kwargs={"tool_calls": openai_tool_calls})
    )
    tool_outputs = example.get("tool_outputs") or [
        "You have correctly called this tool."
    ] * len(openai_tool_calls)
    for output, tool_call in zip(tool_outputs, openai_tool_calls):
        messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))
    return messages


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            BASE_PROMPT,
        ),
        MessagesPlaceholder("examples"),
        ("human", "{text}"),
    ]
)

examples = []
with open(EXAMPLES_PATH, "r", encoding="utf-8") as f:
    examples_json = json.load(f)
    for ex in examples_json["examples"]:
        examples.append((ex["input"], OpportunitySchema.model_validate(ex["output"])))

messages = []

for text, tool_call in examples:
    messages.extend(
        tool_example_to_messages({"input": text, "tool_calls": [tool_call]})
    )

runnable = prompt | llm.with_structured_output(
    schema=OpportunitySchema, include_raw=True
)

with open(MESSAGES_PATH, encoding="utf-8") as f:
    messages_json = json.load(f)


responses = []
for i, msg in enumerate(messages_json["messages"]):
    response = ExtractionResponse()
    try:
        print(f"Processing message {i}")
        resp = runnable.invoke({"text": msg["content"], "examples": messages})
        response.status = ExtractionStatus.SUCCESS
        response.response = resp["parsed"]
        responses.append(response)
    except Exception as e:
        response.status = ExtractionStatus.FAIL
        response.error_message = e.__str__()
        responses.append(response)
    
    print(response.to_json())

#TODO reimplement
def reset_json(path):
    with open(path, "w", encoding="UTF8") as f:
        json.dump({"channel_name": "", "messages": []}, f)


def append_json(responses, path):
    with open(path, "r", encoding="UTF8", newline="") as f:
        json_object = json.load(f)

    with open(path, "w", encoding="UTF8", newline="") as f:
        result = {
            "parameters": {
                "model_name": MODEL_NAME,
                "temperature": TEMPERATURE,
                "max_retries": MAX_RETRIES,
                "base_prompt": BASE_PROMPT
            },
            "responses": [resp.to_json() for resp in responses]
        }
        json_object["results"].append(result)
        json.dump(json_object, f, ensure_ascii=False)
        
append_json(responses, RESULTS_PATH)