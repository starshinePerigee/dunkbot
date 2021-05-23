import os
import asyncio, signal
from dotenv import load_dotenv
import discord



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "dunk" in message.content.lower():
        await message.add_reaction("🏀")
        await message.add_reaction("⤴️")
        await message.add_reaction("🔄")
        await message.add_reaction("☄️")
        await message.add_reaction("🗑️")


async def nice_exit():
    await client.close()
    print("see you space cowboy")


try:
    print("initializing dunks engine")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.start(TOKEN))
except KeyboardInterrupt:
    pass
finally:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(nice_exit())



