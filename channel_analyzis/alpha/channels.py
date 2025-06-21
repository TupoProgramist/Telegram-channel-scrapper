from pyrogram import Client
import json

# Load credentials from config file
with open('../credentials.json', 'r') as f:
    config = json.load(f)

api_id = config['api_id']  # Load from config
api_hash = config['api_hash']  # Load from config

# Create a Pyrogram Client
app = Client("channel_get_posts", api_id=api_id, api_hash=api_hash)

# Function to get 5 posts starting from the Nth one
channels = [
    "@gen_ukraine", "@GrantUP", "@houseofeurope", "@alwaysinomniaparatus", "@internationalyouthopportunities", 
    "@korobova_info", "@KyivAU", "@leadlistt", "@studway_ua", "@seedsofbravery", "@uas_student", 
    "@USAID_AGRO_Ukraine", "@usfofficial", "@unicompass", "@academicjourney", "@kpimobility", 
    "@lawyer_for_NGOs", "@ontherecord", "@interesting_opportunities", "@ngovotum", "@bisnes_communication", 
    "@grants_ukraine", "@grant_opp", "@gurtrc", "@grantsua", "@chegrants", "@grants_here", 
    "@grantovyphishky", "@capabilitiesO", "@uagrants"
]

# Function to get the first 5 posts from each channel
async def get_first_5_posts_and_save():
    async with app:
        # Loop through each channel in the list
        with open(f"posts.txt", 'w', encoding='utf-8') as f:
            for channel_username in channels:
                print(f"Fetching messages from {channel_username}:\n")
                try:
                    # Open a file to save the messages from this channel
                    # Fetch the first 5 posts from the channel
                    async for message in app.get_chat_history(channel_username, limit=5):
                        message_text = message.text if message.text else 'Media/Other Content'
                        print(f"{message_text}")
                        
                        # Save the message text to the file
                        f.write(f"{message_text}\n")
                        f.write(f"-"*20+"\n")
                    print("\n" + "-"*50 + "\n")  # Separator between channels
                except Exception as e:
                    print(f"An error occurred while fetching from {channel_username}: {e}")

# Run the function
app.run(get_first_5_posts_and_save())