import openai
import time
import requests
import json

# def translate(text):
#     url = "http://localhost:5000/translate"
#     payload = {
#     "q": text,  # Text you want to translate
#     "source": "uk",             # Source language (Ukrainian)
#     "target": "en",             # Target language (English)
#     "format": "text"            # Text format (could be 'html' as well)
#     }
#     headers = {
#     "Content-Type": "application/json"
#     }
#     response = requests.post(url, data=json.dumps(payload), headers=headers)

#     if response.status_code == 200:
#     # Parse and print the JSON response
#         result = response.json()
#         return result['translatedText']
#     else:
#         print('X TRANSLATION')
#         return text

def validate_channel(client, posts):
    # Combine the posts into a single string for analysis
    #print(posts)
    combined_posts = "\n".join(posts)
    
    # combined_posts = translate(combined_posts)
    # Prepare the prompt for ChatGPT
    prompt = f"Проаналізуй текст каналу. Він про можливості, стипендії, гранти, фонд,и подібне? \n Відповідь тільки 0 or 1. \n{combined_posts}"
    #print(prompt)
    #try:
    # Call the OpenAI API to get a response from ChatGPT
    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=6000,
        top_p=1,
        stream=False,
        stop=None,
    )
    
    # Get the response text
    answer = completion.choices[0].message
    #response['choices'][0]['message']['content'].strip().lower()
    
    # Validate based on the answer
    return answer.content
    
    # except Exception as e:
    #     print(f"An error occurred while validating the channel: {e}")
    #     return False
