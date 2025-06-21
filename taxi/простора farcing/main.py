from telethon import TelegramClient
from datetime import datetime

# Your API ID and Hash (replace with your own)
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

# Your phone number
phone_number = 'YOUR_PHONE_NUMBER'

# Source channel (the channel you want to copy from)
source_channel_username = 'SOURCE_CHANNEL_USERNAME'

# Target channel (your own channel where you want to copy posts to)
target_channel_username = 'https://t.me/Prostora_archive'

# The date from which to start copying posts (YYYY-MM-DD format)
start_date = datetime.strptime('2023-01-01', '%Y-%m-%d')

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Connect to the client
    await client.start(phone=phone_number)
    print("Client Created")

    # Get the entities of the source and target channels
    source_channel = await client.get_entity(source_channel_username)
    target_channel = await client.get_entity(target_channel_username)

    # Iterate over messages starting from the specified date
    async for message in client.iter_messages(source_channel, min_id=0, offset_date=start_date):
        try:
            # Forward the message to the target channel
            await client.send_message(target_channel, message)
            print(f"Copied message {message.id} from {source_channel_username} to {target_channel_username}")
        except Exception as e:
            print(f"Failed to copy message {message.id}: {e}")

    print("Finished copying messages.")

# Run the client
with client:
    client.loop.run_until_complete(main())
