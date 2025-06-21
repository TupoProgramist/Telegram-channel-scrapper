#here are all the functions, classes, methods for interaction with the telegram
from telethon.sync import TelegramClient
from telethon import functions, types
import json
import time

with open('config.json', 'r') as f:
    config = json.load(f)

# Pause duration between requests (in seconds)
pause_duration = config.get('request_pause', 2)

# get children
def get_children(client, channel_username):
    try:
        # Fetch the channel entity using the username
        channel = client.get_entity(channel_username)

        time.sleep(pause_duration)
        # Fetch recommended channels using the GetChannelRecommendationsRequest
        result = client(functions.channels.GetChannelRecommendationsRequest(
            channel=channel
        ))

        return result.chats  # `result.chats` contains the list of recommended channels

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def initial_parent_upload(client, parent_username):
    try:
        # Fetch the channel object by username
        parent = client.get_entity(parent_username)
        
        time.sleep(pause_duration)
        return parent
    
    except Exception as e:
        print(f"An error occurred while fetching the parent: {e}")
        return None
    
def fetch_first_5_posts(client, channel_username):
    #try:
    posts = []
    # Get the channel entity
    channel = client.get_entity(channel_username)
    
    time.sleep(pause_duration)
    
    # Fetch the first 5 messages
    messages = client.get_messages(channel, limit=5)
    time.sleep(pause_duration)
    if not messages: return None
    
    # Extract the message text from the messages
    for message in messages:
        if message.text: posts.append(message.text)
    
    return posts
    
    #except Exception as e:
    #    print(f"An error occurred while fetching posts: {e}")
    #   return None
