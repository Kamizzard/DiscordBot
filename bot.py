import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


def getRandom(start, end):
    return random.randrange(start, end)

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user.id))

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    if ctx.author == bot.user:
        return
    await ctx.send(f"Hello {ctx.author}!")

@bot.command(description='Responds with the first string input, inputs with spaces require "" quotes')
async def echo(ctx, arg):
    await ctx.send(arg)

@bot.command(description="Command to generate a random number in a range (inclusive).\nFormat: $random rangeStart rangeEnd")
async def rand(ctx, start: int , end: int):
    await ctx.send(f'{getRandom(start, end + 1)}')

@bot.command()
async def d(ctx, number: int):
   await ctx.send(f'{getRandom(1,number + 1)}') 

@bot.command(description="Chooses a reply from 14 options.")
async def magic8(ctx):
    responses = ["Most likely.",
                "It is certain.",
                "Without a doubt.",
                "It is decidedly so.",
                "You may rely on it.",
                "唔係."
                "Don't count on it.",
                "Doubtful.",
                "Outlook not so good.",
                "My reply is no.",
                "Concentrate and ask again.",
                "Better not tell you now.",
                "https://klipy.com/gifs/monkey-tongue-monkey-lala"
                ]
    await ctx.send(f"{responses[getRandom(0, (len(responses)))]}")

load_dotenv()
token = os.getenv('DISCORD_API_TOKEN')
bot.run(token)