# Discord bot with discord.py test 1
# wrtten with the assistance of:
# https://boostlog.io/@junp1234/how-to-write-a-discord-bot-in-python-5a8e73aca7e5b7008ae1da8b
# by plscks
#
# Maybe this will work?
# Uses exclusively python 3.6
# Uses discord.py rewrite:
# python -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
# Good luck!!
import argparse
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.', desciption='A bot that greets the user back')

# Maybe? I don't know what I'm doing...
parser = argparse.ArgumentParser('Discord Bot Test1')
parser.add_argument('-t', '--token', help='Your bots token', action='store', dest='token')
args = parser.parse_args()
token = args.token
print(args)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#@bot.command()
#async def craft(ctx, item):
    
    
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":eggplant: Why hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="plscks#0156")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    # embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name=".add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name=".multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name=".greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name=".cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name=".info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name=".help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run(token)
