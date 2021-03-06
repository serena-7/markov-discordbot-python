import os
import discord
from markov import make_chains, make_text

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    text_content = message.content
    chains = make_chains(text_content)
    new_message = make_text(chains)

    await message.channel.send(new_message)

client.run(os.environ['DISCORD_TOKEN'])
