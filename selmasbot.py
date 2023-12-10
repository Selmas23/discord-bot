#Importing class libraries with discord, importing token files, operating system and randomly generate something

import discord
import os
import random
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

load_dotenv()

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#Created a client object from the discord class and insterted the token

client = discord.Client()
token = str(os.getenv('SELMA'))

#Initalizing Bot

@client.event 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client))

#Setting bot responses to user messages
#If elif functions to return random motivational quotes or sayings

@client.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 

    print(f'Message {user_message} by {username} on {channel}') 
#if
    if message.author == client.user: 
        return

    if channel == "random": 
        if user_message.lower() == "hello" or user_message.lower() == "hi": 
            await message.channel.send(f'Hello {username}') 
            return
        elif user_message.lower() == "bye": 
            await message.channel.send(f'Bye {username}') 
        elif user_message.lower() == "motivate me": 
            motivation = [" You can do this!",
                    "Dont give up! Keep pushing.", 
                    "No pressure, No diamonds.", 
                    "The only thing that overcomes hard luck is hard work."] 
            await message.channel.send(random.choice(motivation)) 

        elif user_message.lower() == 'hello world':
            await message.channel.send('hello')

        elif user_message.lower() == ("tell me about your server"):
            await message.channel.send(f"""your ec2 server data:\n
region:{ec2_metadata.region}\n
public ipv4 address:{ec2_metadata.public_ipv4}\n
availability zone:{ec2_metadata.availability_zone}\n
server instance:{ec2_metadata.instance_type}""")
        else:
            await message.channel.send(f"I'm sorry, the command '{user_message}' is not a valid command")

#Bot begins running
client.run(token)
