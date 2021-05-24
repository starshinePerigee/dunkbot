import discord


class DunkClient:
    def __init__(self):
        print("initializing dunks engine")
        self.client = discord.Client()

        self.initialize_events()

    def initialize_events(self):
        @self.client.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(self.client))

        @self.client.event
        async def on_message(message):
            if message.author == self.client:
                return

            if "dunk" in message.content.lower():
                await message.add_reaction("🏀")
                await message.add_reaction("⤴️")
                await message.add_reaction("🔄")
                await message.add_reaction("☄️")
                await message.add_reaction("🗑️")

    async def nice_exit(self):
        await self.client.close()
        print("see you space cowboy")

