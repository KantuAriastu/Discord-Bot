# bot.py
import os
import re
import discord
from dotenv import load_dotenv
from conversion import *
import re 

regex = r"(\d+\s*)(centi|cm|mm|mili|km|kilo|meter|m)"
length_find = re.compile(regex)

load_dotenv()
token = "NjM2NzMwOTIzODc3OTI0ODcw.XdoWXw.awYOC8TdB70R3H6aCZknIinEiKU"


dad_joke = ("I Am", "I am" "I'm", "Am", "Aku","aku" ,"Im", "aing", "Aing", "gw")
base_length = ("centi","cm","mm","mili","km","kilo","meter","m")

class MyClient(discord.Client):
    

    async def on_message(self, message):
        if message.author == client.user:
            return
            
        print('Message from {0.author}: {0.content}'.format(message))
        
        #for ident in dad_joke :
        #    if ident in message.content :
        #        x = message.content.find(ident)
        #        msg2send = message.content[x+len(ident):]
        #        await message.channel.send("Hi "+msg2send+", I'm Dad")

        matched = length_find.findall(message.content)
        if matched :
            await message.channel.send("fun fact")
            for x,unit in matched :
                length = lengthconv(float(x),unit)
                length.randomconversion()
                msg = length.msgconstruct()
                await message.channel.send(msg)


        
            
        

client = MyClient()
client.run(token)



