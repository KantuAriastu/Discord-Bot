# bot.py
import os
import re
import discord
from dotenv import load_dotenv




load_dotenv()
token = os.getenv('DISCORD_TOKEN')


dad_joke = ("I Am", "I am" "I'm", "Am", "Aku","aku" ,"Im", "aing", "Aing", "gw")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
            
        print('Message from {0.author}: {0.content}'.format(message))
        
        for ident in dad_joke :
            if ident in message.content :
                x = message.content.find(ident)
                msg2send = message.content[x+len(ident):]
                await message.channel.send("Hi "+msg2send+", I'm Dad")


client = MyClient()
client.run(token)



