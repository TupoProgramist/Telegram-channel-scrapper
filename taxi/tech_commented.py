import openai

# Function to get API response from OpenAI
# This function interfaces with OpenAI's ChatGPT API to analyze Telegram channel content
# and determine if it contains opportunities (grants, scholarships, internships, etc.)
def get_chatgpt_response(prompt, api_key):
    """
    Sends a prompt to OpenAI's ChatGPT API and returns the response.
    
    Args:
        prompt (str): The text to be analyzed by the AI model
        api_key (str): OpenAI API authentication key
    
    Returns:
        str: The AI's response content, stripped of whitespace
    """
    # Set the API key for authentication with OpenAI services
    openai.api_key = api_key
    
    # Create a chat completion request using GPT-3.5-turbo model
    # This model is cost-effective and suitable for text classification tasks
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # System message defines the AI's role and behavior
            {"role": "system", "content": "You are a helpful assistant."},
            # User message contains the actual content to be analyzed
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract and return the AI's response, removing leading/trailing whitespace
    return response['choices'][0]['message']['content'].strip()

def main():
    """
    Main function that handles user interaction and coordinates the AI analysis process.
    This serves as a simple interface for testing AI-based channel content validation.
    """    # API key placeholder - in production, this should be loaded from a secure config file
    # or environment variable to avoid hardcoding sensitive credentials
    api_key = 'YOUR_OPENAI_API_KEY'
    
    # Get user input - in the broader project context, this would be replaced with
    # automated text extraction from Telegram channels
    user_input = input("Please enter your input string: ")
    
    # Send the user's input to ChatGPT for analysis
    # This function call validates whether the input content relates to opportunities
    response = get_chatgpt_response(user_input, api_key)
    
    # Display the AI's analysis results to the user
    # In the full system, this would feed into automated channel classification
    print("ChatGPT response:")
    print(response)

# Entry point - ensures main() only runs when script is executed directly,
# not when imported as a module in the larger project ecosystem
if __name__ == "__main__":
    main()
