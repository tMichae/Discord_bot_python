import discord
from discord.ext import commands

TOKEN = "token"

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(TOKEN)