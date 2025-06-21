import openai
import time
import requests
import json

with open('credentials.json', 'r') as f:
    credentials = json.load(f)
    
openai.api_key = credentials.get('openai_api_key')
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

 

def validate_channel(posts, open = True, client=None):
    # Combine the posts into a single string for analysis
    #print(posts)
    combined_posts = "\n".join(posts)
    
    # combined_posts = translate(combined_posts)
    # Prepare the prompt for ChatGPT
    prompt = f"Проаналізуй цей текст. Він про можливості, такі як гранти, стипендії, конкурси, курси, ресурси для стартапів, соціальних ініціатив, обмінів або академічних проєктів? Аудиторія: студенти, науковці, соціальні активісти, молодь, стартапери, які шукають можливості для розвитку. Це НЕ мають бути: новини, блог, продаж. Якщо інформації замало - не підходитьІ. Відповідь тільки 0 або 1. \n{combined_posts}"
    #print(prompt)
    #try:
    # Call the OpenAI API to get a response from ChatGPT
    if open:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You evaluate Telegram chanels."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=3,
            temperature=0.3
        )
        answer = response.choices[0].message.content.strip()
        # answer = "1"
    else:
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
        answer = completion.choices[0].message.content
        #response['choices'][0]['message']['content'].strip().lower()
        
    # Validate based on the answer
    return answer
    
    # except Exception as e:
    #     print(f"An error occurred while validating the channel: {e}")
    #     return False
