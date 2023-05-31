# Building Your Own Morning Greeting Slack Bot: A Step-by-Step Tutorial

The goal of this project is to build a friendly "good morning" bot on Slack. In essence, the idea is to create a bot that will greet everyone on the team every weekday morning at 9:00am. This little project aims to teach us how to create a project from scratch, use Slack's API, and schedule tasks.

But this isn't just about adding some cheer to our mornings; it's also an approachable way to learn coding and automation. Using Python, a user-friendly programming language popular among beginners, we're going to learn how to interact with the Slack API and how to schedule tasks. We'll also learn how to deploy our bot to Heroku, a cloud platform that will allow us to run our bot 24/7.

By creating this bot, we'll see firsthand how automation can make our lives easier. Our bot will never forget to say "Good Morning!" - no matter if it's a busy Monday or a quiet holiday. It's a simple way to demonstrate the power of automation in handling routine tasks, giving us more time and mental space to focus on more important, complex problems.

Once we've got the hang of creating our morning greeting bot, we'll see how we can tweak and add to it. Maybe we'll make it share a fun fact for the day, or remind us about important events. This project serves as a stepping stone, showing us that with a little bit of learning and creativity, we can build tools that bring our virtual workspaces to life.

## Prerequisites

Before we get started, we'll need to make sure we have a few things set up:

- Slack Workspace: You need to have a Slack workspace where you can create and add your bot. If you don't already have one, you can create it for free on the Slack website.
- Python: Basic knowledge of Python programming is needed as we'll be using it to write our bot. If you're completely new to Python, there are numerous resources online where you can learn it.
- Python Environment: You'll need a Python environment set up on your computer. This project uses Python 3, so ensure you have it installed.
- Slack API: Familiarity with APIs (Application Programming Interfaces) would be beneficial, specifically Slack's API, as it will be used to make our bot interact with Slack.
- pip (Python Package Installer): pip is used to install Python packages. We'll use it to install the slack_sdk and schedule Python libraries. It usually comes pre-installed with Python.
- Heroku Account: Lastly, if you plan on deploying your bot to run continuously, you'll need an account on a platform like Heroku. You can sign up for free and deploy one bot without any cost.

## How to create a Python virtual environment step-by-step

**Ensure Python is installed**

First, ensure that Python is installed on your system. You can do this by typing the following command into your terminal or command prompt:

```bash 
python --version
```


**Install the virtualenv package**

Python includes a built-in module for creating virtual environments since version 3.4. If you are using a version older than 3.4, you will need to use the virtualenv package. You can install it using pip, Python's package manager, with the following command:

```bash
pip install virtualenv
```

**Create the virtual environment**

To create a virtual environment, navigate to the directory where you want to create the virtual environment and type the following command:

```bash
python -m venv myvenv
```

You can replace 'myenv' with any name you prefer. This will create a new directory with the name you specified, which will contain the Python executable files and a copy of the pip library. In my case, i will use slack-bot as the name of my virtual environment.

**Activate the virtual environment**

Before you can start installing or using packages in your virtual environment, you'll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell's PATH.

On Windows, the following command will activate the virtual environment:

```bash
myvenv\Scripts\activate
```

On Unix or MacOS, the following command will activate the virtual environment:

```bash
source myvenv/bin/activate
```

You should see the name of your virtual environment in brackets on your terminal line e.g. (myvenv).

**Deactivate the virtual environment**

To deactivate the virtual environment, simply type the following command:

```bash
deactivate
```

This will return you to your global Python environment.


## How to create a Slack app step-by-step

**Create a Slack app**

1. Visit the Slack API website: https://api.slack.com/apps?new_app=1
2. Click on the 'Create an App' button, next click on 'From scratch'.
3. A dialog box will appear. You can give your app a name (like "Good Morning Bot") and select the workspace where you want the app to reside. Then click 'Create App'.

**Configure the app**

1. Once your app is created, you'll be taken to the 'Basic Information' page. Scroll down to the 'Display Information' section and add a short description, icon for your app and background color.
2. Save your changes.

**Install the App to Your Workspace**

Before your app can interact with your workspace, it needs to be installed.

1. On the sidebar, click on 'Install App'.
2. Click on "Please add at least one feature or permission scope to install your app."
   - From the main page of your Slack app, select "OAuth & Permissions", "scopes" and click on OAuth Scopes and select call:write and chat:write.
3. Click on 'Install App to Workspace'.
4. Slack will ask for permissions. Click 'Allow'.


**Get the Bot Token**

After installing the app, you'll need to get the bot token. This token is used to authenticate your bot in the code that you'll write.

1. Go to the 'OAuth & Permissions' page in the sidebar.
2. Look for the 'Bot Token' section. You should see a token that begins with 'xoxb-'.
3. Copy this token and save it somewhere safe. You'll need to add it to your Python code.

Remember, this token is sensitive information and provides access to your Slack workspace. ***Do not share it with anyone or post it publicly.***

We can now move on to writing the code for our bot, ¡yei!

Once you've written the code, you can invite the bot to any channel in your workspace by typing /invite **@YourBotName** in the channel. The bot will then be able to read and write messages in this channel.

My Bot is called **@good-morning-bot** and it is in the channel **#general**.

## Python code step-by-step

Now it's time to write some Python code, and I'll walk you through it step by step.

Let's start by creating a file, and you can use your favorite code editor, mine is Visual Studio Code. I've created a file called slackbot.py and I will add the necessary libraries.

```python
import os
import schedule
import time
from slack_sdk import WebClient
```

Next, you need to initialize a client that will communicate with Slack. Replace 'bot-token' with the bot token you obtained earlier.


```python
slack_token = 'bot-token'  # Replace 'bot-token' with your actual bot token
client = WebClient(token=slack_token)
```

Now, we will define a function to send a "Good Morning" message to a specific channel. Replace 'your-channel-id' with the ID of the channel where you want to send the message.

```python
def send_message():
    client.chat_postMessage(
      channel='your-channel-id', # Replace 'your-channel-id' with the actual ID of your channel
      text="Good Morning, team! :coffee:"
    )
```

Now we're going to use the schedule library to schedule our send_message function to run at 9:00am every weekday.

```python
schedule.every().day.at("21:48").do(send_message)
```

Finally, we'll add a loop that will run our scheduled tasks every 10 seconds. This will allow our bot to check if it's time to send a message.

```python
while True:
    schedule.run_pending()
    time.sleep(10)
```

Finally, the magic happens and all you need to do is type python **slackbot.py** into the console.

Now your bot should send a "Good Morning" message to your specified channel at 9:00am every weekday.

Please note, you need to keep your script running continuously for the scheduling to work. In the next step, you'll learn how to deploy your bot to Heroku so it can run 24/7.


## Random greetings

Now that we have our bot sending a "Good Morning" message every weekday, let's make it a little more interesting by adding some variety to the message. 

**Create a Text File with the Greetings**

Create a text file, say greetings.txt, and add different "Good morning" messages on separate lines, in my case, I speak Spanish and I want to send some messages in my language.

Good morning, team! Hope you have a great day!
¡Hola!, buenos días y excelente día para todos.
Hello everyone, good morning! Let's have a productive day!
Good morning, folks! Let's make today count!
Buenas!!, ship it! :shipit:

Next, you need to update your Python script to read from this file and randomly select a greeting to send. We'll use the random library to do this.

```python
import random
```

And then we'll update our send_message function to read from the file and select a random greeting.

```python

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
```

Finally, we have the update and we are going to run the file again.

```bash
python slackbot.py
```

And there you have it - your very own Slack bot to deliver a friendly "Good Morning" message to your team every weekday. 

### Test mode

If you want to test your bot without having to wait until 9:00am, you can change the schedule to run every minute. This will allow you to test your bot and make sure it's working as expected.

```python
schedule.every().minute.do(send_message)
```

Also I recommend you to use the following code to test your bot.

```python
if __name__ == "__main__":
    send_message()
```

And then you can run the file again.

```bash
python slackbot.py
```

In the other case, you can use the test mode from Slack.

https://api.slack.com/methods/conversations.list/test

You just need to provide your token and you will get the list of channels in your workspace. If you have some errors you can saw something like:

```
{
    "ok": false,
    "error": "missing_scope",
    "needed": "channels:read,groups:read,mpim:read,im:read",
    "provided": "calls:write,chat:write"
}
```

## Conclusion

This is a practical way to see how automation can make our lives easier and lear more about Python. I hope you enjoyed this tutorial and that you can use it to build your own Slack bot.

You can see the complete code in my GitHub repository:


In my next post, I'll show you how to deploy your bot to Heroku so it can run 24/7.

Happy coding!




