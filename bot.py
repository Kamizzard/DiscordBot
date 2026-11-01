import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, description="Discord bot for fun and games")


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user.id))


@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)
# @bot.event
# async def onCommandError(ctx, error):
#     if isinstance(error, commands.errors.CommandNotFound):
#         await ctx.send("Command not found.\nPlease try $help for a list of commands.")

async def main():
    await bot.load_extension("cogs.maincog")

asyncio.run(main())
load_dotenv()
token = os.getenv('DISCORD_API_TOKEN')
bot.run(token)