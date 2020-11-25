import discord

async def run(client, message):
    if message.content.startswith("!echo"):
        msg = ' '.join(message.content.split(" ")[1:]
        await message.channel.send(f"Echo : {msg}")
    if message.content == "!hello":
        await message.channel.send(f"Hi! My name is {client.user.name}.")

content_key = ["!hello"]
startswith_key = ["!echo"]
