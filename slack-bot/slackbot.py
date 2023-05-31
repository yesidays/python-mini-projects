# Slack Bot - Medium

import os
import schedule
import time
import datetime
from slack_sdk import WebClient

import random

# Create a slack client
slack_token = 'bot-token' 
client = WebClient(token=slack_token)

'''
# Just one message
def send_message():
    weekday = datetime.datetime.now().weekday()
    if weekday < 5:  # 0-4 corresponds to Monday to Friday
        client.chat_postMessage(
            channel='your-channel-id',
            text="Good Morning, team! :coffee:"
        )
'''

def send_message():
    weekday = datetime.datetime.today().weekday()
    if weekday < 5:  # 0-4 corresponds to Monday to Friday
        with open('greetings.txt', 'r') as file:
            greetings = file.read().splitlines()
    
        random_greeting = random.choice(greetings)

        client.chat_postMessage(
          channel='your-channel-id',
          text=random_greeting
        )

schedule.every().day.at("9:00").do(send_message)


while True:
    schedule.run_pending()
    time.sleep(10)

