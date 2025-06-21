import openai

# Function to get API response from OpenAI
def get_chatgpt_response(prompt, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def main():    # API key placeholder - should be loaded from environment variable or config file
    api_key = 'YOUR_OPENAI_API_KEY'
    
    # Ask the user for an input string
    user_input = input("Please enter your input string: ")
    
    # Send the input as a prompt to ChatGPT
    response = get_chatgpt_response(user_input, api_key)
    
    # Display the response in the console
    print("ChatGPT response:")
    print(response)

if __name__ == "__main__":
    main()