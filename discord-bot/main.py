#import
import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
import random

#constants
sadWords = ["sad", "depressed", "crappy", "upset", "angry"]
happyWords = ["happy", "jolly", "yay", "yippee", "yipee", "yahoo", "yayy", "glad"]
sadResponses = ["haha", "ok", "no way bro"]
happyResponses = ["not happy for you", "ok", ":)", "sure"]
youtubeWords = ["youtube", "YouTube", "Youtube", "yt", "Yt", "YT"]
coinflips = ["heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","heads", "tails","what the heck!!! the coin got swallowed up into the depths of hell!!"]
ytLinks = ["https://youtu.be/MUGqM_HSqi0?si=VykPqwC162iI6h3X", "https://youtu.be/-q0clpZMHrw?si=dAu9QL0UUORumnzu", "https://youtu.be/IOcehCFJTmM?si=J1SsIknQWGmK0QHf", "https://youtu.be/lSv0cDcCOlI?si=9lJTbcvV9rUoXrFP"]

#events
@client.event
async def on_ready():
    print("We have logged in as {0.user}"
    .format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hi'):
        await message.channel.send('hello')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if any(word in message.content for word in sadWords):
        response = random.choice(sadResponses)
        await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if any(word in message.content for word in happyWords):
        response = random.choice(happyResponses)
        await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if any(word in message.content for word in youtubeWords):
        ytLink = random.choice(ytLinks)
        response = "did someone say youtube? heres yoptube "+ ytLink
        await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!coinflip'):
        response = random.choice(coinflips)
        await message.channel.send("flipping that coin...")
        await message.channel.send(response)

        
#run
client.run("OTc1MDQzNjk1Njg0NDg1MjE1.Gti8Xq.iOffvj-luxFG43MKVIhIW4b_wD048Ebvivd8-0")