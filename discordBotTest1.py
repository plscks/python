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

bot = commands.Bot(command_prefix='.', desciption='A bot that does bot stuff maybe?')

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
async def mats(ctx, *, comp='list'):
    comp = comp.lower()
    mats = {}
    mats['bag of industrial plastic'] = '''```Weight: 4\n+--------------------+--------+--------+---------+
|                    |  Find  |    %   |    %    |
|      Location      | Weight | Chance | chance/ |
|                    |        |        |    AP   |
+--------------------+--------+--------+---------+
| Junkyard(O)        |    4   |  10.5  |   4.74  |
+--------------------+--------+--------+---------+
| Stygian Foundry(I) |   10   |   7.4  |   2.21  |
+--------------------+--------+--------+---------+
| Factory(I)         |   10   |   7.3  |   2.19  |
+--------------------+--------+--------+---------+
| Warehouse(I)       |    1   |   4.2  |   1.25  |
+--------------------+--------+--------+---------+```'''
    mats['batch of leather'] = '''```Weight: 2\n+--------------------+--------+--------+---------+
|                    |  Find  |    %   |    %    |
|      Location      | Weight | Chance | chance/ |
|                    |        |        |    AP   |
+--------------------+--------+--------+---------+
| Stygian Foundry(I) |   10   |   7.4  |   2.21  |
+--------------------+--------+--------+---------+
| Factory(I)         |   10   |   7.3  |   2.19  |
+--------------------+--------+--------+---------+```'''
    mats['batch of mushrooms'] = '''```Weight: 1\n+-------------------+--------+--------+---------+
|                   |  Find  |    %   |    %    |
|      Location     | Weight | Chance | chance/ |
|                   |        |        |    AP   |
+-------------------+--------+--------+---------+
| Forest(O)         |   40   |  17.4  |   3.48  |
+-------------------+--------+--------+---------+
| Idyllic Forest(O) |   40   |   14   |   2.81  |
+-------------------+--------+--------+---------+
| Lush Orchard(O)   |    5   |  12.5  |   2.50  |
+-------------------+--------+--------+---------+
| Ruins(O)          |   30   |  10.5  |   1.57  |
+-------------------+--------+--------+---------+
| Grassland(O)      |    5   |   5.8  |   0.87  |
+-------------------+--------+--------+---------+
| Field(O)          |    5   |   5.8  |   1.16  |
+-------------------+--------+--------+---------+
| Park(O)           |    5   |   5.5  |   0.82  |
+-------------------+--------+--------+---------+
| Orchard(O)        |    5   |   5.3  |   1.05  |
+-------------------+--------+--------+---------+
| Maintain(O)       |    1   |    2   |   0.40  |
+-------------------+--------+--------+---------+```'''
    mats['blood ice'] = '''```Weight: 1\nNumber of Uses: 1\nCrafted: By Defilers by using the Life Vampire skill on a victim, or by Desecrating a corpse (one of several random \n         results). Blood Ice cannot be created via Alchemical Transmutation.\nAdditional Effect: Good-aligned or Neutral-aligned characters lose 1 point of Morality with each use.\nHealing: 20 Hit Points\n+---------------------------+--------+--------+---------+
|                           |  Find  |    %   |    %    |
|          Location         | Weight | Chance | chance/ |
|                           |        |        |    AP   |
+---------------------------+--------+--------+---------+
| Dark Harem(I)             |    5   |   2.8  |   0.56  |
+---------------------------+--------+--------+---------+
| Ebony Tower(I)            |    2   |   2.3  |   0.70  |
+---------------------------+--------+--------+---------+
| Great Ziggurat(I)         |    5   |    2   |   0.39  |
+---------------------------+--------+--------+---------+
| Dark Sanitarium(I)        |    1   |   0.8  |   0.17  |
+---------------------------+--------+--------+---------+
| Black Prison(I)           |    1   |   0.6  |   0.13  |
+---------------------------+--------+--------+---------+
| Damned Library(I)         |    1   |   0.6  |   0.22  |
+---------------------------+--------+--------+---------+
| Hall of Reconstruction(I) |    1   |   0.5  |   0.15  |
+---------------------------+--------+--------+---------+```'''
    mats['bottle of holy water'] = '''```Weight: 1\n+---------------------------+--------+--------+---------+
|                           |  Find  |    %   |    %    |
|          Location         | Weight | Chance | chance/ |
|                           |        |        |    AP   |
+---------------------------+--------+--------+---------+
| Euphoria Asylum(I)        |   14   |    12  |   2.39  |
+---------------------------+--------+--------+---------+
| Church(I)                 |   20   |   8.3  |   1.65  |
+---------------------------+--------+--------+---------+
| Vault of Enlightenment(I) |   14   |   7.4  |   2.22  |
+---------------------------+--------+--------+---------+
| Panopticon(I)             |    5   |   4.9  |   0.98  |
+---------------------------+--------+--------+---------+
| Ward of Respite(I)        |    5   |   3.2  |   0.96  |
+---------------------------+--------+--------+---------+```'''
    mats['bottle of paradise water'] = '''```Weight: 1\n+---------------------------+--------+--------+---------+
|                           |  Find  |    %   |    %    |
|          Location         | Weight | Chance | chance/ |
|                           |        |        |    AP   |
+---------------------------+--------+--------+---------+
| Mill(I)                   |   15   |  42.9  |   8.57  |
+---------------------------+--------+--------+---------+
| Ivory Tower(I)            |   10   |  13.5  |   4.05  |
+---------------------------+--------+--------+---------+
| Panopticon(I)             |   10   |   9.8  |   1.96  |
+---------------------------+--------+--------+---------+
| Euphoria Asylum(I)        |   10   |   8.5  |   1.71  |
+---------------------------+--------+--------+---------+
| Vault of Enlightenment(I) |   10   |   5.3  |   1.59  |
+---------------------------+--------+--------+---------+
| Ward of Respite(I)        |    5   |   3.2  |   0.96  |
+---------------------------+--------+--------+---------+```'''
    mats['bunch of daisies'] = '''```Weight: 1\n+-----------------+--------+--------+---------+
|                 |  Find  |    %   |    %    |
|     Location    | Weight | Chance | chance/ |
|                 |        |        |    AP   |
+-----------------+--------+--------+---------+
| Grassland(O)    |   20   |  23.3  |   3.49  |
+-----------------+--------+--------+---------+
| Orchard(O)      |   20   |  21.1  |   4.21  |
+-----------------+--------+--------+---------+
| Park(O)         |   12   |  13.2  |   1.98  |
+-----------------+--------+--------+---------+
| Lush Orchard(O) |    5   |  12.5  |   2.50  |
+-----------------+--------+--------+---------+
| Forest(O)       |   20   |   8.7  |   1.74  |
+-----------------+--------+--------+---------+
| Idyllic Forest  |   20   |    7   |   1.4   |
+-----------------+--------+--------+---------+
| Mountain(O)     |    1   |    2   |   0.40  |
+-----------------+--------+--------+---------+
| Bakery(O)       |    1   |   0.7  |   0.40  |
+-----------------+--------+--------+---------+```'''
    mats['bunch of lilies'] = '''```Weight: 1\n+-------------------+--------+--------+---------+
|                   |  Find  |    %   |    %    |
|      Location     | Weight | Chance | chance/ |
|                   |        |        |    AP   |
+-------------------+--------+--------+---------+
| Ruins(O)          |   20   |    7   |   1.05  |
+-------------------+--------+--------+---------+
| Park(O)           |    5   |   5.5  |   0.82  |
+-------------------+--------+--------+---------+
| Forest(O)         |    5   |   2.2  |   0.43  |
+-------------------+--------+--------+---------+
| Mountain(O)       |    1   |    2   |   0.40  |
+-------------------+--------+--------+---------+
| Idyllic Forest(O) |    5   |   1.8  |   0.35  |
+-------------------+--------+--------+---------+```'''
    mats['bunch of paradise lilies'] = '''```Weight: 1\n+----------------------+--------+--------+---------+
|                      |  Find  |    %   |    %    |
|       Location       | Weight | Chance | chance/ |
|                      |        |        |    AP   |
+----------------------+--------+--------+---------+
| Idyllic Grassland(O) |    5   |  26.3  |   3.95  |
+----------------------+--------+--------+---------+
| Idyllic Forest(O)    |   30   |  10.5  |   2.11  |
+----------------------+--------+--------+---------+```'''
    mats['chunk of brass'] = '''```Weight: 2\n+--------------------+--------+--------+---------+
|                    |  Find  |    %   |    %    |
|      Location      | Weight | Chance | chance/ |
|                    |        |        |    AP   |
+--------------------+--------+--------+---------+
| Smithy(I)          |   14   |  16.1  |   4.83  |
+--------------------+--------+--------+---------+
| Stygian Foundry(I) |   20   |  14.7  |   4.41  |
+--------------------+--------+--------+---------+
| Factory(I)         |   20   |  14.6  |   4.38  |
+--------------------+--------+--------+---------+
| Junkyard(O)        |    4   |  10.5  |   4.74  |
+--------------------+--------+--------+---------+
| Warehouse(I)       |    1   |   4.2  |   1.25  |
+--------------------+--------+--------+---------+```'''
    mats['chunk of iron'] = '''```Weight: 2\n+--------------------+--------+--------+---------+
|                    |  Find  |    %   |    %    |
|      Location      | Weight | Chance | chance/ |
|                    |        |        |    AP   |
+--------------------+--------+--------+---------+
| Junkyard(O)        |    4   |  10.5  |   4.74  |
+--------------------+--------+--------+---------+
| Warehouse(I)       |    1   |   4.2  |   1.25  |
+--------------------+--------+--------+---------+
| Stygian Foundry(I) |    5   |   3.7  |   1.10  |
+--------------------+--------+--------+---------+
| Factory(I)         |    5   |   3.6  |   1.09  |
+--------------------+--------+--------+---------+
| Mountain(O)        |    1   |    2   |   0.40  |
+--------------------+--------+--------+---------+```'''
    mats['chunk of ivory'] = '''```Weight: 1\n+---------------------------+--------+--------+---------+
|                           |  Find  |    %   |    %    |
|          Loaction         | Weight | Chance | Chance/ |
|                           |        |        |    AP   |
+---------------------------+--------+--------+---------+
| Euphoria Asylum(I)        |   20   |  17.1  |   3.42  |
+---------------------------+--------+--------+---------+
| Ivory Tower(I)            |   10   |  13.5  |   4.05  |
+---------------------------+--------+--------+---------+
| Panopticon(I)             |   10   |   9.8  |   1.96  |
+---------------------------+--------+--------+---------+
| Ward of Respite(I)        |   15   |   9.6  |   2.87  |
+---------------------------+--------+--------+---------+
| Vault of Enlightenment(I) |   10   |   5.3  |   1.59  |
+---------------------------+--------+--------+---------+
| Museum(I)                 |    8   |   3.4  |   1.03  |
+---------------------------+--------+--------+---------+```'''
    mats['chunk of onyx'] = '''```Weight: 1\n+-----------+--------+--------+---------+
|           |  Find  |    %   |    %    |
|  Loaction | Weight | Chance | Chance/ |
|           |        |        |    AP   |
+-----------+--------+--------+---------+
| Museum(I) |    8   |   3.4  |   1.03  |
+-----------+--------+--------+---------+```'''
    mats['chunk of steel'] = '''```Weight: 2\n+-----------------------+--------+--------+---------+
|                       |  Find  |    %   |    %    |
|        Loaction       | Weight | Chance | Chance/ |
|                       |        |        |    AP   |
+-----------------------+--------+--------+---------+
| Iron Wastes(O)        |    5   |  33.3  |   6.67  |
+-----------------------+--------+--------+---------+
| Argentium Remnants(O) |    5   |  33.3  |   6.67  |
+-----------------------+--------+--------+---------+
| Stygian Foundry(I)    |   30   |  22.1  |   6.62  |
+-----------------------+--------+--------+---------+
| Factory(I)            |   30   |  21.9  |   6.57  |
+-----------------------+--------+--------+---------+
| Smithy(I)             |   15   |  17.2  |   5.16  |
+-----------------------+--------+--------+---------+
| Junkyard(O)           |    5   |  13.2  |   5.92  |
+-----------------------+--------+--------+---------+
| Warehouse(I)          |    1   |   4.2  |   1.25  |
+-----------------------+--------+--------+---------+```'''
    mats['chunk of stygian iron'] = '''```Weight: 2\n+--------------------+--------+--------+---------+
|                    |  Find  |    %   |    %    |
|      Loaction      | Weight | Chance | Chance/ |
|                    |        |        |    AP   |
+--------------------+--------+--------+---------+
| Iron Wastes(O)     |   10   |  66.7  |  13.33  |
+--------------------+--------+--------+---------+
| Firepits(O)        |   10   |  15.4  |   3.08  |
+--------------------+--------+--------+---------+
| Dark Sanitarium(I) |   10   |   8.4  |   1.68  |
+--------------------+--------+--------+---------+
| Egg Field(O)       |   10   |   7.7  |   1.15  |
+--------------------+--------+--------+---------+
| Black Prison(I)    |   10   |   6.4  |   1.27  |
+--------------------+--------+--------+---------+
| Great Ziggurat(I)  |   10   |   3.9  |   0.78  |
+--------------------+--------+--------+---------+```'''
    mats['femur'] = '''```Weight: 2\n+---------------------------+--------+--------+---------+
|                           |  Find  |    %   |    %    |
|          Loaction         | Weight | Chance | Chance/ |
|                           |        |        |    AP   |
+---------------------------+--------+--------+---------+
| Boneland(O)               |    5   |  33.3  |  26.67  |
+---------------------------+--------+--------+---------+
| Frozen Wastes(O)          |    5   |  26.3  |   3.95  |
+---------------------------+--------+--------+---------+
| Dark Harem(I)             |   25   |   14   |   2.79  |
+---------------------------+--------+--------+---------+
| Dark Sanitarium(I)        |   15   |  12.6  |   2.52  |
+---------------------------+--------+--------+---------+
| Great Ziggurat(I)         |   25   |   9.8  |   1.96  |
+---------------------------+--------+--------+---------+
| Black Prison(I)           |   15   |   9.6  |   1.91  |
+---------------------------+--------+--------+---------+
| Hall of Reconstruction(I) |   15   |   7.4  |   2.21  |
+---------------------------+--------+--------+---------+
| Ebony Tower(I)            |    5   |   5.8  |   1.74  |
+---------------------------+--------+--------+---------+
| Ruins(O)                  |   10   |   3.5  |   0.52  |
+---------------------------+--------+--------+---------+
| Damned Library(I)         |    5   |   3.1  |   1.09  |
+---------------------------+--------+--------+---------+```'''
    mats['gold ingot'] = '''```Weight: 3\n+--------------------+--------+--------+---------+
|                    |  Find  |    %   |    %    |
|      Loaction      | Weight | Chance | Chance/ |
|                    |        |        |    AP   |
+--------------------+--------+--------+---------+
| Bank(I)            |   10   |  18.2  |   5.45  |
+--------------------+--------+--------+---------+
| Parliament(I)      |    1   |   6.7  |   1.33  |
+--------------------+--------+--------+---------+
| Euphoria Asylum(I) |    5   |   4.3  |   0.85  |
+--------------------+--------+--------+---------+
| Museum(I)          |    8   |   3.4  |   1.03  |
+--------------------+--------+--------+---------+
| Office Building(I) |    1   |   3.1  |   0.94  |
+--------------------+--------+--------+---------+
| Mansion(I)         |    8   |   2.6  |   0.79  |
+--------------------+--------+--------+---------+
| Beach(O)           |    1   |   0.9  |   0.19  |
+--------------------+--------+--------+---------+```'''
    mats['handful of grave dirt'] = '''```Weight: 1\n+-------------+--------+--------+---------+
|             |  Find  |    %   |    %    |
|   Loaction  | Weight | Chance | Chance/ |
|             |        |        |    AP   |
+-------------+--------+--------+---------+
| Cemetary(O) |   20   |  23.5  |   3.53  |
+-------------+--------+--------+---------+```'''
    mats['humerus'] = '''```Weight: 2\n+---------------------------+--------+--------+---------+
|                           |  Find  |    %   |    %    |
|          Loaction         | Weight | Chance | Chance/ |
|                           |        |        |    AP   |
+---------------------------+--------+--------+---------+
| Boneland(O)               |    5   |  33.3  |  26.67  |
+---------------------------+--------+--------+---------+
| Egg Field(O)              |   24   |  18.5  |   2.77  |
+---------------------------+--------+--------+---------+
| Dark Harem(I)             |   24   |  13.4  |   2.68  |
+---------------------------+--------+--------+---------+
| Soul Orchard(I)           |   14   |  12.6  |   2.52  |
+---------------------------+--------+--------+---------+
| Dark Sanitarium(I)        |   14   |  11.8  |   2.35  |
+---------------------------+--------+--------+---------+
| Hall of Reconstruction(I) |   24   |  11.8  |   3.53  |
+---------------------------+--------+--------+---------+
| Great Ziggurat(I)         |   24   |   9.4  |   1.88  |
+---------------------------+--------+--------+---------+
| Black Prison(I)           |   14   |   8.9  |   1.78  |
+---------------------------+--------+--------+---------+
| Firepits(O)               |    5   |   7.7  |   1.54  |
+---------------------------+--------+--------+---------+
| Ebony Tower(I)            |    5   |   5.8  |   1.74  |
+---------------------------+--------+--------+---------+
| Ruins(O)                  |   10   |   3.5  |   0.52  |
+---------------------------+--------+--------+---------+
| Damned Library(I)         |    5   |   3.1  |   1.09  |
+---------------------------+--------+--------+---------+```'''
    if comp in mats:
        await ctx.send('**' + comp + '**\n' + mats[comp])
    elif comp == 'list':
        fulllist = '\n•'.join(list(mats.keys()))
        embed = discord.Embed(title='Usage:', description="'.mats <MATERIAL_NAME>' to list available crafting materials\n (must be exact item name)", color=0x00BFFF)
        embed.add_field(name='Materials:', value='•' + fulllist)
        await ctx.send(embed=embed)
    else:
        await ctx.send('Item **' + comp + '** not recognozed.')
        
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
        embed = discord.Embed(title='Usage:', description="'.craft <ITEM_NAME>' to list crafting XP and requirements\n (must be exact item name)", color=0x00BFFF)
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
    await ctx.send(":eggplant: Why hello, there! <:kitty:491077122434138124>")

@bot.command()
async def cat(ctx):
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
    embed = discord.Embed(title="__**Nexus Clash RRFBot**__", description="*An ever evolving Nexus Clash RRFBot. List of commands are:*", color=0xeee657)

    #embed.add_field(name=".add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    #embed.add_field(name=".multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False1)
    embed.add_field(name=".craft", value="Gives crafting info of items, use '.craft list' to list all items", inline=False)
    embed.add_field(name=".mats", value="Gives info on how to obtain crafting materials", inline=False)
    embed.add_field(name=".greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name=".cat", value="Gives a cute fORB gif to lighten up the mood???.", inline=False)
    embed.add_field(name=".info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name=".help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

if __name__ == '__main__':
    token = parse()
    bot.run(token)
