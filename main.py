import discord
import logging
from discord.ext import commands
import random
import setup as s

bot = commands.Bot(command_prefix=s.prefix, description=s.description)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))


@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined the server on {0.joined_at}'.format(member))


@bot.command()
async def exit():
    """Exits the bot instance"""
    await bot.say('Shutting down now...')
    await bot.close()


@bot.command()
async def on_join():
    """Posts a welcome message for every new member joining the server"""
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}'
    await bot.say(fmt.format(member, server))


if __name__ == '__main__':
    bot.run(s.token)

