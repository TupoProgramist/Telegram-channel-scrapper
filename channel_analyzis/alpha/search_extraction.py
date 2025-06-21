from alpha.extraction_schemas import OpportunitySchema
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_retries=4,
    disable_streaming=True,
)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. Your task is to extract only the relevant information from the provided text and return it in valid JSON format. "
            "For each attribute, extract the value based on the information available in the text. If an attribute's value is not explicitly mentioned or cannot be determined, return null or an empty list (depending on the attribute's description). "
            "Ensure the extracted information is written in perfect Ukrainian without any spelling or grammatical errors. Proper names, such as names of people, organizations, and locations, should be extracted as-is and not translated. "
            "Only provide the requested fields: `type`, `audience`, `field_name`, and `location`. The values can have multiple hypotheses if necessary, and examples are provided but not strictly required:\n\n"
            "type: The type of opportunity (e.g., 'Scholarship', 'Internship', 'Conference').\n"
            "audience: The target audience (e.g., 'Students', 'Researchers', 'Entrepreneurs').\n"
            "field_name: The field or discipline related to the opportunity (e.g., 'STEM', 'Business', 'Engineering').\n"
            "location: The geographical location of the event (e.g., 'Kyiv', 'Online'). If the event is online, extract 'Online'.\n\n"
            "Here is the user's description:\n{{text}}\n\n"
            "Output the result in **JSON format only**, following this structure:\n\n"
            "{{\n"
            "  \"type\": \"string or null\",\n"
            "  \"audience\": [\"array of strings or empty\"],\n"
            "  \"field_name\": [\"array of strings or empty\"],\n"
            "  \"location\": \"string or null\"\n"
            "}}\n"
            "There are examples of processed user queries: \n"
            "{examples}"
        ),
        ("human", "{query}"),
    ]
)

runnable = prompt | llm.with_structured_output(schema=OpportunitySchema, include_raw=True, method="json_mode")

import json
with open("./search_examples.json", "r", encoding='utf-8') as f:
    examples = json.load(f)["examples"]
    
query = "Мені потрібні безплатні курси/тренінги для Проект менеджменту"

response = runnable.invoke({"query": query, "examples": examples})

print(response["parsed"].model_dump())