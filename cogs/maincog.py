import discord
from discord.ext import commands
import random

class MainCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        if ctx.author == self.bot.user:
            return
        await ctx.send(f"Hello {ctx.author}!")

    @commands.command(description='Responds with the first string input, inputs with spaces require "" quotes')
    async def echo(self, ctx, arg):
        await ctx.send(arg)

    @commands.command()
    async def echo2(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)}ms.')


    @commands.command(description="Command to generate a random number in a range (inclusive).\nFormat: $random rangeStart rangeEnd")
    async def rand(self, ctx, start: int , end: int):
        await ctx.send(f'{random.randrange(start, end + 1)}')


    @commands.command()
    async def d(self, ctx, number: int):
        await ctx.send(f'{random.randrange(1,number + 1)}') 


    @commands.command(description="Chooses a reply from 14 options.")
    async def magic(self, ctx):
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
        await ctx.send(f"{responses[random.randrange(0, (len(responses)))]}")


async def setup(bot):
    await bot.add_cog(MainCog(bot))