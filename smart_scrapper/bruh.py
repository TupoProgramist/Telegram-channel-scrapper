from telethon.sync import TelegramClient
from telethon import functions, types
import json

# Load credentials from config file
with open('config.json', 'r') as f:
    config = json.load(f)

with TelegramClient("bruh", config['api_id'], config['api_hash']) as client:
    result = client(functions.channels.GetChannelRecommendationsRequest(
        channel='@pragmatikamedia'
    ))

    # Accessing the chats attribute of the result
    for channel in result.chats:
        print(channel.title)
