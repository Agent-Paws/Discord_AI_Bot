# bot.py
import math
import os
import io
import random
import discord
import datetime

from discord import opus
from discord.ext.commands import Bot, has_permissions, CheckFailure, MissingPermissions
from discord.ext import commands

TOKEN = 'NjU5ODc1Mzc4ODQzODc3Mzc2.XgUq1g.KBLotmxVavARiock7ycdd9i5Ce8'

client = commands.Bot(command_prefix='~')

civmemes = ['https://i.kym-cdn.com/photos/images/original/001/119/185/4b6.jpg',
            'https://rmcphersonnarrativedesign.files.wordpress.com/2017/01/6d0.jpg?w=500']

oof = [
       'https://images-na.ssl-images-amazon.com/images/I/61IwNTw0fCL._SY355_.png']

actually = ['https://i.imgur.com/cZ6BadH.jpg',
            'https://i.kym-cdn.com/photos/images/newsfeed/001/191/035/135.png']

nice = ['https://media2.giphy.com/media/nLH7f5K1Tb1sY/giphy.gif',
        'https://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif',
        'https://media1.tenor.com/images/874306570ecbc115f2031b1d10f0c52e/tenor.gif?itemid=13228431']

gandhi = ['https://i.kym-cdn.com/photos/images/newsfeed/000/614/225/273.jpg',
          'https://i.imgflip.com/159ltz.jpg',
          'http://m.quickmeme.com/img/04/044f664c67c293ad221d15a377942809ca93cf7ab4b8408c136ab095b1da9cac.jpg',
          'https://s4.scoopwhoop.com/anj/sdbb/615438237.jpg',
          'https://i.imgur.com/3jRx5do.jpg']

mad = ['https://media.makeameme.org/created/im-mad-5c3371.jpg',
       'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTi67z3AWYwbHQjjSprw7sF6xD-ASLnMeiGHOs6LiL3tEyjMOYqYw&s',
       'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDgFpGvJX7PS8TMOpeKcRcucMpc0RvbF360x8hyQfMIA49uuG2&s',
       'https://i.pinimg.com/originals/bf/ff/0e/bfff0e2365bb82bef646aa9d56664d7a.jpg']

league = ['https://tenor.com/view/pizza-steve-league-players-gif-18914725', ]

sad = ['https://tenor.com/view/veggietales-gif-5224526',
       ]

fight = ['https://tenor.com/view/boxing-box-punch-hit-fight-gif-5393841',
         ]

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


@client.event
async def on_ready():
    guilds = list(client.guilds)
    print(f'{client.user} is connected to the following guilds:\n')
    for guild in guilds:
        print(f'{guild.name}(id: {guild.id})')


@client.event
async def on_member_join(member):
    server = member.guild
    channel = discord.utils.get(server.channels, name="general")

    await member.send(f'{member.mention} Welcome to {server.name}')
    if server.name == 'Nikolay\'s Jew Camp':
        await channel.send(f'Hello {member.mention}, Welcome to the server')
    else:
        await channel.send(f'Hello {member.mention}, Welcome to the server')

    f = open('member_joins.txt', 'a')
    f.write(f'{member} has joined 'f'{server.name}(id: {server.id}) \n')
    f.close()


@client.event
async def on_member_remove(member):
    server = member.guild
    channel = discord.utils.get(server.channels, name="general")
    nchannel = discord.utils.get(server.channels, name="gas-chambers7")

    if server.name == 'Nikolay\'s Jew Camp':
        await nchannel.send(f'{member} dipshit left ')
    else:
        await channel.send(f'{member} Bye ')

    f = open('member_joins.txt', 'a')
    f.write(f'{member} has left {server.name}(id: {server.id}) \n')
    f.close()


@client.event
async def on_message(message):
    server = message.guild
    member = message.author
    channel = message.channel
    logchannel = client.get_channel(663429414507380786)
    x = datetime.datetime.now()

    if message.author.bot:
        if channel.name != 'log':
            with io.open("bot_logs.log", "a", encoding="utf-8") as f:
                f.write(
                    f'{x} : {member} wrote:\n  "{message.content}"\nin {channel.id} {server.name}(id: {server.id}) \n')
            f.close()
    else:
        with io.open("chat_logs.log", "a", encoding="utf-8") as f:
            f.write(f'{x} : {member} wrote: "{message.content}" in {channel.name} {server.name}(id: {server.id}) \n')
            if channel.name != 'jew-bot':
                await logchannel.send(
                    f'{x} : **{member}** wrote: **"{message.clean_content}"** ---- {channel.name} ---- {server.name}(id: {server.id}) \n')
        f.close()
    await client.process_commands(message)


@client.listen()
async def on_message(message):
    member = message.author
    channel = message.channel
    nik = '<@175915247989686272>'
    dan = '<@175915198287314944>'
    mich = '<@324653924416094212>'
    kacp = '<@96289155050381312>'
    tomat = '<@242332338887852042>'

    if channel.name != 'log':
        if not message.author.bot:
            if 'hairline' in message.content.lower():
                await channel.send(f'{mich} lost his hairline at child birth')
            elif 'one leg' in message.content.lower():
                await channel.send(f'{kacp} lost his leg during the vietnam war')
            elif 'forehead' in message.content.lower():
                await channel.send(f'{kacp}\'s can be used as a reflector! ')
            elif message.content.lower() == 'nice':
                await channel.send(random.choice(nice))
            elif message.content.lower() == 'ya yeet':
                await channel.send('https://i.gifer.com/RIb.gif')
            elif 'racist' in message.content.lower():
                await channel.send('https://media1.tenor.com/images/b29f1ad912e0e1154d9c2d7ff815a013/tenor.gif?itemid=4929147')
            elif message.content.lower() == 'mich is dumb':
                await channel.send('i agree')
            elif 'ayy lmao' in message.content.lower():
                await channel.send('https://i.ytimg.com/vi/kiEqGhgWf5Y/maxresdefault.jpg')
            elif 'mad ' in message.content.lower():
                await channel.send(random.choice(mad))
            elif 'fight' in message.content.lower():
                await channel.send(random.choice(fight))
            elif 'smh' in message.content.lower():
                await channel.send('https://i.imgflip.com/bnuop.jpg')
            elif 'who are you' in message.content.lower():
                await channel.send('https://thumbs.gfycat.com/UntidyMemorableBangeltiger-small.gif')
            elif 'actually' in message.content.lower():
                await channel.send(random.choice(actually))
            elif 'oof' in message.content.lower():
                await channel.send(random.choice(oof))
            elif 'sad' in message.content.lower():
                await channel.send(random.choice(sad))
            elif 'gandhi' in message.content.lower():
                await channel.send(random.choice(gandhi))
            elif 'egg' in message.content.lower():
                await channel.send('https://i.redd.it/4aibmandzgu21.jpg')
            elif 'one more turn' in message.content.lower():
                await channel.send(random.choice(civmemes))
            elif 'perhaps' in message.content.lower():
                await channel.send('https://i.redd.it/qh7mgkucu2y21.jpg')
            elif 'spoken' in message.content.lower():
                await channel.send('https://media.tenor.com/images/8a34a9befd5b4b726a6b14d21c041176/tenor.gif')
            elif 'analysis' in message.content.lower():
                await channel.send('https://media1.tenor.com/images/a1486d5a56353d73eda51c72ce2e1bd7/tenor.gif?itemid=12855053')
            elif 'fuck you' in message.content.lower():
                await channel.send(f'{member.mention} no you')
            elif 'leeg' in message.content.lower():
                await channel.send(random.choice(league))
            elif 'nik' in message.content.lower():
                emojis = ["🇫", "🇦", "🇹"]
                for emoji in emojis:
                    await message.add_reaction(emoji)
            elif 'dan' in message.content.lower():
                emojis = ["🗿", "🚭"]
                for emoji in emojis:
                    await message.add_reaction(emoji)
            elif 'sophie' in message.content.lower():
                emojis = ["🇩", "🇼", "🇦", "🇷", "🇫"]
                for emoji in emojis:
                    await message.add_reaction(emoji)
            elif 'mich' in message.content.lower():
                emojis = ["🇵", "🇪", "🇩", "🇴"]
                for emoji in emojis:
                    await message.add_reaction(emoji)
            elif 'jude' in message.content.lower():
                emojis = ["🅱️", "🇴", "🇲", "🇧"]
                for emoji in emojis:
                    await message.add_reaction(emoji)
            elif 'max' in message.content.lower():
                emojis = ["🇸", "🇦", "🇩", "◾", "🇫", "🇺", "🇨", "🇰", "◼", "🇧", "🇴", "🇾"]
                for emoji in emojis:
                    await message.add_reaction(emoji)
            elif 'alex' in message.content.lower():
                emojis = ["🇦","➡️","🇿"]
                for emoji in emojis:
                    await message.add_reaction(emoji)
            elif 'baniil' in message.content.lower():
                emojis = ["🇬","🇦","🇾"]
                for emoji in emojis:
                    await message.add_reaction(emoji)
            elif 'kacp' in message.content.lower():
                await message.add_reaction("◻️")
            else:
                pass


@client.event
async def on_command_error(ctx, error):
    # if command has local error handler, return
    if hasattr(ctx.command, 'on_error'):
        return

    # get the original exception
    error = getattr(error, 'original', error)

    if isinstance(error, commands.CommandNotFound):
        return

    if isinstance(error, commands.BotMissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' and '.join(missing)
        _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)
        await ctx.send(_message)
        return

    if isinstance(error, commands.DisabledCommand):
        await ctx.send('This command has been disabled.')
        return

    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
        return

    if isinstance(error, commands.MissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = ' and '.join(missing)
        _message = 'You need the **{}** permission(s) to use this command.'.format(fmt)
        await ctx.send(_message)
        return

    if isinstance(error, commands.UserInputError):
        await ctx.send("Invalid input.")
        return

    if isinstance(error, commands.NoPrivateMessage):
        try:
            await ctx.author.send('This command cannot be used in direct messages.')
        except discord.Forbidden:
            pass
        return

    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permission to use this command.")
        return


# COMMANDS


@client.command(help='| Responds with "Sup Bitch"')
async def hello(ctx):
    await ctx.send("sup")


@client.command(help="| Checks Latency")
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')
    print(f'Ping is: {round(client.latency * 1000)}ms')


@client.command(help="| Clears inputted amount of messages or 5 by default")
@has_permissions(administrator=True)
async def clear(ctx, amount=5):
    member = ctx.message.author
    if amount <= 0:
        await ctx.send(f'Enter a value greater than 0 {member.mention}, ROGER ROGER')
        print(f'{member} has entered a value less than 0 for clear')
    else:
        amount += 1
        await ctx.channel.purge(limit=amount)
        amount += -1
        await ctx.send(f'Bot has cleared {amount} messages for {member.mention}, ROGER ROGER')
        print(f'Bot has cleared {amount} messages for {member}')


@client.command(help='| R.I.P')
async def order66(ctx):
    bot = ctx.me
    await ctx.send("https://www.youtube.com/watch?v=xSN6BOgrSSU")
    await bot.edit(nick='DARTH Sidious')
    await ctx.send("Commander Cody, the time has come. Execute Order Sixty-Six. ", tts=True)
    await ctx.channel.purge(limit=1)
    await bot.edit(nick='CLONE COMMANDER CODY')
    await ctx.send("It will be done, My Lord.", tts=True)
    await ctx.channel.purge(limit=1)
    await bot.edit(nick='Droid')
    await ctx.send("Roger Roger", tts=True)
    await ctx.channel.purge(limit=1)


@client.command(help='| R.I.P', hidden=True)
async def clap(ctx):
    bot = ctx.me
    await bot.edit(nick='Cupid')
    await ctx.send("Have you met the one yet?", tts=True)
    await ctx.channel.purge(limit=2)
    await bot.edit(nick='Droid')


@client.command(help='| R.I.P', hidden=True)
async def shakira(ctx):
    bot = ctx.me
    await bot.edit(nick='Meehow')
    await ctx.send("SHAKIRA SHAKIRA", tts=True)
    await ctx.channel.purge(limit=2)
    await bot.edit(nick='Droid')


@client.command(help='| leave a conversation', hidden=False)
async def leave(ctx):
    await ctx.channel.purge(limit=1)
    member = ctx.message.author
    await ctx.send(f'{member.mention} has left the conversation')


@client.command(help='| join a conversation ', hidden=False)
async def join(ctx):
    await ctx.channel.purge(limit=1)
    member = ctx.message.author
    await ctx.send(f'{member.mention} has joined the conversation')

@client.command(help='| no ', hidden=True)
async def no(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'no')

@client.command(help='| yes ', hidden=True)
async def yes(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'yes')




client.run(TOKEN)
