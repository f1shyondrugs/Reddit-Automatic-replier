import os
import praw
import time
from discord_webhook import DiscordWebhook
from datetime import datetime

webhookurl = "YOUR WEBHOOK URL"

def reply():
    client_id = 'CLIENT_ID'
    client_secret = 'CLIENT_SECRET'
    username = 'YOUR USERNAME'
    password = 'YOUR ACCOUNT PASSWORD'
    user_agent = 'YOUR AGENT NAME'

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent=user_agent
    )


    folder_path = 'chatgpt/'

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                post_link = lines[0].strip()

                rest_of_lines = ''.join(lines[1:]).strip()

                submission = reddit.submission(url=post_link)
                submission.reply(rest_of_lines)
                
                print(f"Comment added to {post_link}.")

                now = datetime.now()

                current_time = now.strftime("%H:%M:%S")
                webhook = DiscordWebhook(url=webhookurl,
                                         content=f"Comment added to {post_link}. ({current_time})\n{rest_of_lines}")
                response = webhook.execute()

