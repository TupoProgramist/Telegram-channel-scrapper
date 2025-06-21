#this is the sandbox
from telethon.sync import TelegramClient
from telethon import functions, types
import json
import sqlite3
from telethon.sync import TelegramClient
from telethon.errors import UsernameNotOccupiedError, UsernameInvalidError
import database
import telegram
import AI
import os
import time

from groq import Groq

#load credetials for telegrm requests
#load configurations
def load_json(adress):
    with open(adress, 'r', encoding='utf-8') as file:
        value = json.load(file)
        return value
    
# upload all parents from txt file
def initial_parents_upload_txt(adress):
    try:
        with open(adress, 'r') as file:
            parents_usernames = [line.strip() for line in file if line.strip()]
        return parents_usernames
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# upload all parents to DATABASE
def initial_parent_upload(file_path, conn, client):
    cursor = conn.cursor()
    
    parents_usernames = initial_parents_upload_txt(file_path)
    
    for parent_username in parents_usernames:
        parent = telegram.initial_parent_upload(client, parent_username)
        
        database.initial_parent_upload(conn, parent)

#get some parent from a txt file
def get_parent(adress):
    with open(adress, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Take the first line and remove it
    parent = lines[0]
    lines = lines[1:]
    
    # Open the file in write mode and save the remaining lines
    with open(adress, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    
    return parent, len(lines)

#make new children
def expand(conn, client):
    while 1:
            
            #get the name of unparsed parent
            parent_username = database.get_unparsed_parent_username(conn)
            
            #Are there parents left
            if parent_username == None:
                #print("E| No parents found")
                break
            
            #get parent's children
            children = telegram.get_children(client, parent_username)
            
            if children == None:
                print("E| No children found")
                continue
            
            for child in children:
                if child.username == None:
                    print("E| Child is None")
                    continue
                
                database.insert_child(conn, parent_username, child)
            
            #making is_parced flag 1
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE Chats
            SET is_parced = 1
            WHERE username = ?
            ''', (parent_username,))
            conn.commit()

channels = ["PLkosmetika", "unicef_spilno_IronLand", "beketov_senat", "saudi_for_business", "educationusaukraine"
]

try:
    if __name__ == '__main__':
        config = load_json("config.json")
        cred = load_json("credentials.json")
        #ai = Groq()

        
        conn = sqlite3.connect("chats.db")
        conn.row_factory = sqlite3.Row
        
        with TelegramClient(cred["session_name"], cred["api_id"], cred["api_hash"]) as client:
            client.start()
            while 1:
                
                #get the name of unvalidated
                channel_username = database.get_unvalidated_channel_username(conn)
                #channel_username = database.get_deleted_channel_username(conn)
                #Are there parents left
                if channel_username == None:
                    print("E| No channels left")
                    break
                #get channels first 5 posts
                posts = telegram.fetch_first_5_posts(client, channel_username)
                
                if posts == None:
                    print("E| No posts found")
                    continue
                
                valide = AI.validate_channel(posts)
                cursor = conn.cursor()
                
                if valide == '1':
                    #making is_parced flag 1
                    print(f"{channel_username}: V")
                    cursor.execute('''
                    UPDATE Chats
                    SET is_verified = 1
                    WHERE username = ?
                    ''', (channel_username,))
                    # channel = telegram.initial_parent_upload(client, channel_username)
                    # database.initial_parent_upload(conn,channel)
                else:
                    print(f"{channel_username} | X")
                    print(f"↑{valide}↑")
                    cursor.execute('''
                    INSERT INTO deleted (username)
                    VALUES (?)
                    ''', (channel_username,))
                    cursor.execute('''
                    DELETE FROM Chats WHERE username = ?
                    ''', (channel_username,))
                    # cursor.execute('''
                    # INSERT INTO del_del (username)
                    # VALUES (?)
                    # ''', (channel_username,))
                # cursor.execute('''
                # DELETE FROM deleted WHERE username = ?
                # ''', (channel_username,))
                conn.commit()
            
            # database.reset_database(conn)
            #initial_parent_upload("channels/parents.txt", conn, client)
            #goind through all the parents
        
                
        conn.close()
finally:
    # Always disconnect in the finally block
    client.disconnect()