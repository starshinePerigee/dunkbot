import os
import asyncio
from dotenv import load_dotenv
import discord

from dunks import dunkbot

print("loading bots...")
load_dotenv()
DUNK_TOKEN = os.getenv('DUNK_TOKEN')


dunk_client = dunkbot.DunkClient()


try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dunk_client.client.start(DUNK_TOKEN))
except KeyboardInterrupt:
    pass
finally:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dunk_client.nice_exit())
