import discord
from options import vocab
import random

client = discord.Client()


def run():
    token = "NDUxMDgxNDc3MzUxMDE0NDEy.DqlNNA.C8_7wRH9zuGYfDqt34eNid80z1k"
    print("starting...")
    client.run(token)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.lower() in vocab.flip():
        await msg.channel.send(random.choice(["cara", "coroa"]))

    if msg.content.lower() in vocab.dado():
        await msg.channel.send(random.choice(["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]))


run()
