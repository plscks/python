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

def parse():
    # Maybe? I don't know what I'm doing...
    parser = argparse.ArgumentParser('Discord Bot Test1')
    parser.add_argument('-t', '--token', help='Your bots token', action='store', dest='token')
    args = parser.parse_args()
    token = args.token
    return token

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.command()
async def craft(ctx, *, item='list'):
    item = item.lower()
    craft = {}
    craft.setdefault('carving knife', []).append('+4xp / +2AP')
    craft.setdefault('carving knife', []).append('1 Chunk of Steel')
    craft.setdefault('chainsaw', []).append('+14xp / +7AP')
    craft.setdefault('chainsaw', []).append('2 Chunk of Steel')
    craft.setdefault('chainsaw', []).append('1 Length of Chain')
    craft.setdefault('chainsaw', []).append('2 Bag of Industrial Plastic')
    craft.setdefault('cutlass', []).append('+10xp / +5AP')
    craft.setdefault('cutlass', []).append('2 Chunk of Steel')
    craft.setdefault('cutlass', []).append('1 Chunk of Brass')
    craft.setdefault('hatchet', []).append('+6xp / +3AP')
    craft.setdefault('hatchet', []).append('1 Chunk of Iron')
    craft.setdefault('hatchet', []).append('1 Piece of Wood')
    craft.setdefault('rapier', []).append('+10xp / +5AP')
    craft.setdefault('rapier', []).append('2 Chunk of Steel')
    craft.setdefault('rapier', []).append('1 Chunk of Iron')
    craft.setdefault('sabre', []).append('+10xp / +5AP')
    craft.setdefault('sabre', []).append('2 Chunk of Steel')
    craft.setdefault('sabre', []).append('1 Chunk of Iron')
    craft.setdefault('sword', []).append('+10xp / +5AP')
    craft.setdefault('sword', []).append('3 Chunk of Steel')
    craft.setdefault('tarnished sword', []).append('+10xp / +5AP')
    craft.setdefault('tarnished sword', []).append('2 Chunk of Steel')
    craft.setdefault('tarnished sword', []).append('1 Silver Ingot')
    craft.setdefault('torch', []).append('+8xp / +4AP')
    craft.setdefault('torch', []).append('1 Piece of Wood')
    craft.setdefault('torch', []).append('1 Batch of Leather')
    craft.setdefault('torch', []).append('1 Length of Rope')
    craft.setdefault('torch', []).append('1 Chunk of Brass')
    craft.setdefault('chainmail shirt', []).append('+20xp / +10AP')
    craft.setdefault('chainmail shirt', []).append('4 Chunk of Steel')
    craft.setdefault('fireman\'s jacket', []).append('+10xp / +5AP')
    craft.setdefault('fireman\'s jacket', []).append('2 Batch of Leather')
    craft.setdefault('fireman\'s jacket', []).append('1 Bag of Industrial Plastic')
    craft.setdefault('leather cuirass', []).append('+4xp / +2AP')
    craft.setdefault('leather cuirass', []).append('3 Batch of Leather')
    craft.setdefault('leather jacket', []).append('+4xp / +2AP')
    craft.setdefault('leather jacket', []).append('2 Batch of Leather')
    craft.setdefault('plate cuirass', []).append('+20xp / +10AP')
    craft.setdefault('plate cuirass', []).append('4 Chunk of Steel')
    craft.setdefault('plate cuirass', []).append('2 Batch of Leather')
    craft.setdefault('suit of light body armor', []).append('+20xp / +10AP')
    craft.setdefault('suit of light body armor', []).append('2 Batch of Leather')
    craft.setdefault('suit of light body armor', []).append('3 Bag of Industrial Plastic')
    craft.setdefault('suit of military encounter armor', []).append('+30xp / +15AP')
    craft.setdefault('suit of military encounter armor', []).append('4 Bag of Industrial Plastic')
    craft.setdefault('suit of military encounter armor', []).append('2 Batch of Leather')
    craft.setdefault('suit of police riot armor', []).append('+20xp / +10AP')
    craft.setdefault('suit of police riot armor', []).append('2 Batch of Leather')
    craft.setdefault('suit of police riot armor', []).append('3 Bag of Industrial Plastic')
    craft.setdefault('flamethrower', []).append('+16 xp / +8AP')
    craft.setdefault('flamethrower', []).append('4 Chunk of Steel')
    craft.setdefault('flamethrower', []).append('1 Bag of Industrial Plastic')
    craft.setdefault('pistol', []).append('+8xp / +4AP')
    craft.setdefault('pistol', []).append('1 Chunk of Brass')
    craft.setdefault('pump action shotgun', []).append('+16xp / +8AP')
    craft.setdefault('pump action shotgun', []).append('3 Chunk of Steel')
    craft.setdefault('pump action shotgun', []).append('1 Chunk of Brass')
    craft.setdefault('pump action shotgun', []).append('1 Piece of Wood')
    craft.setdefault('rifle', []).append('+16xp / +8AP')
    craft.setdefault('rifle', []).append('5 Chunk of Steel')
    craft.setdefault('rifle', []).append('1 Chunk of Brass')
    craft.setdefault('rifle', []).append('1 Piece of Wood')
    craft.setdefault('sub-machine gun', []).append('+12xp / +6AP')
    craft.setdefault('sub-machine gun', []).append('2 Chunk of Steel')
    craft.setdefault('sub-machine gun', []).append('1 Chunk of Brass')
    craft.setdefault('long bow', []).append('+14xp / +7AP')
    craft.setdefault('long bow', []).append('3 Piece of Wood')
    craft.setdefault('short bow', []).append('+6xp / +3AP')
    craft.setdefault('short bow', []).append('1 Piece of Wood')
    craft.setdefault('sling', []).append('+8xp / +4AP')
    craft.setdefault('sling', []).append('2 Batch of Leather')
    craft.setdefault('compound bow', []).append('+10xp / +5AP')
    craft.setdefault('compound bow', []).append('2 Piece of Wood')
    craft.setdefault('compound bow', []).append('1 Bag of Industrial Plastic')
    if item in craft:
        final = '\n•'.join(craft[item])
        embed = discord.Embed(title=item, description=final, color=0x00BFFF)
        await ctx.send(embed=embed)
    elif item == 'list':
        fulllist = '\n•'.join(list(craft.keys()))
        embed = discord.Embed(title='Usage:', description="'.craft <ITEM_NAME>' to list rafting XP and requirements\n (must be exact item name)", color=0x00BFFF)
        embed.add_field(name='Craftable Items:', value='•' + fulllist)
        await ctx.send(embed=embed)
    else:
        await ctx.send('Item **' + item + '** not recognozed as craftable')
        
@bot.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)
    print(arg)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":eggplant: Why hello, there! :kitty:")

@bot.command()
async def fORB(ctx):
    await ctx.send("https://78.media.tumblr.com/335ffa43ca4a5e8201381912debcf880/tumblr_inline_pac9jri0Yi1vzg9ht_500.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="A Current work in progress.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="plscks")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    # embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="An ever evolving plscksBot. List of commands are:", color=0xeee657)

    #embed.add_field(name=".add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    #embed.add_field(name=".multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False1)
    embed.add_field(name=".craft", value="Gives crafting info of items, use '.craft list' to list all items", inline=False)
    embed.add_field(name=".greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name=".fORB", value="Gives a cute fORB gif to lighten up the mood???.", inline=False)
    embed.add_field(name=".info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name=".help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

if __name__ == '__main__':
    token = parse()
    bot.run(token)
