import discord
import logging
from discord.ext import commands
import random
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
disc_token = config.get('DISCORD', 'token')
prefix = config.get('DISCORD', 'prefix')
description = config.get('DISCORD', 'description')

bot = commands.Bot(command_prefix=prefix, description=description)
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


@bot.listen
async def on_join(member: discord.Member):
    """Posts a welcome message for every new member joining the server"""
    await bot.say('Welcome to the server {0.user}! Please enjoy your stay'.format(member))


if __name__ == '__main__':
    bot.run(disc_token)
