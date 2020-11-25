import discord
from handler import Handler

import config

client = discord.Client()
mHandler = Handler(client=client, directory="modules", prefix="!", help_command=True)

@client.event
async def on_ready():
    print(client.user.name)

@client.event
async def on_message(message):
    await mHandler.process_messages(message)

client.run(config.token)
