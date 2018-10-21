import discord
from commands.vocab import Vocab as vocab
import random
import Token
from commands import command

client = discord.Client()


def run():
    print("starting...")
    client.run(Token.get())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    a = command.run(msg.content.lower())
    await msg.channel.send(a)


run()
