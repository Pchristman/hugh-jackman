import random

import discord
import os

bot = discord.Client()

@bot.event
async def on_message(message):
    if str(message.author) == "elisgotjokes#9550" or "eli" in message.content:
        x = random.randint(1, 10)
        if x == 1:
            await message.channel.send("Eli...I want you to know I'm disappointed in you.")
        elif x == 2:
            await message.channel.send("Someday Eli will go far. Personally, I hope he stays there.")
        elif x == 3:
            await message.channel.send("Eli is the reason God created the middle finger.")
        elif x == 4:
            await message.channel.send("Eli brings everyone so much joy. You know, when he leaves the room. But still.")
        elif x == 5:
            await message.channel.send("I thought of Eli today. It reminded me to take out the trash.")
        elif x == 6:
            await message.channel.send("Eli, just want to say you look great today. Not at all like you usually look")
        elif x == 7:
            await message.channel.send("Somewhere out there is a tree tirelessly producing oxygen for Eli. He owes it an apology")
        elif x == 8:
            await message.channel.send("If genius skips a generation, then Eli's kids will be brilliant")
        elif x == 9:
            await message.channel.send("Eli is proof that evolution can go in reverse.")
        else:
            await message.channel.send("Anyone ever notice how Eli smells like hot dog water?")




bot.run(os.getenv("TOKEN"))

