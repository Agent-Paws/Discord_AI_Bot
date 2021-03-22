# bot.py
import math
import os
import io
import random
import discord
import datetime
import chatbot_framework

from discord import opus
from discord.ext.commands import Bot, has_permissions, CheckFailure, MissingPermissions
from discord.ext import commands
from dotenv import load_dotenv
from collections import namedtuple

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='~')
i = 0


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

    f = open('member_joins.txt', 'a')
    f.write(f'{member} has joined 'f'{server.name}(id: {server.id}) \n')
    f.close()


@client.event
async def on_member_remove(member):
    server = member.guild
    channel = discord.utils.get(server.channels, name="general")

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
                    f'{x} : **{member}** wrote: **"{message.clean_content}"** ---- {channel.name} ---- {server.name}(id: {server.id}) \n')
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
    question = str(message.content)

    response = chatbot_framework.response(question)
    if channel.name != 'log':
        if not message.author.bot:
            if response:
                if str(response[1]) == 'Text':
                    await channel.send(response[0])
                elif str(response[1]) == 'Emoji':
                    emojis = list(response[0].split(" "))
                    for emoji in emojis:
                        await message.add_reaction(emoji)
                else:
                    # print(chatbot_framework.response(question))
                    pass


# @client.event
# async def on_command_error(ctx, error):
#     # if command has local error handler, return
#     if hasattr(ctx.command, 'on_error'):
#         return
#
#     # get the original exception
#     error = getattr(error, 'original', error)
#
#     if isinstance(error, commands.CommandNotFound):
#         return
#
#     if isinstance(error, commands.BotMissingPermissions):
#         missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
#         if len(missing) > 2:
#             fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
#         else:
#             fmt = ' and '.join(missing)
#         _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)
#         await ctx.send(_message)
#         return
#
#     if isinstance(error, commands.DisabledCommand):
#         await ctx.send('This command has been disabled.')
#         return
#
#     if isinstance(error, commands.CommandOnCooldown):
#         await ctx.send("This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
#         return
#
#     if isinstance(error, commands.MissingPermissions):
#         missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
#         if len(missing) > 2:
#             fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
#         else:
#             fmt = ' and '.join(missing)
#         _message = 'You need the **{}** permission(s) to use this command.'.format(fmt)
#         await ctx.send(_message)
#         return
#
#     if isinstance(error, commands.UserInputError):
#         await ctx.send("Invalid input.")
#         return
#
#     if isinstance(error, commands.NoPrivateMessage):
#         try:
#             await ctx.author.send('This command cannot be used in direct messages.')
#         except discord.Forbidden:
#             pass
#         return
#
#     if isinstance(error, commands.CheckFailure):
#         await ctx.send("You do not have permission to use this command.")
#         return


# COMMANDS

my_dict = {'username': 'counter'}

@client.command(pass_context=True)
async def votekick(ctx, userName: discord.User):

    if userName.name not in my_dict:
        my_dict.update({userName.name: 1})
    else:
        my_dict[userName.name] += 1

    await ctx.send(f'{my_dict[userName.name]}/4 people have voted to kick {userName.display_name}')

    if my_dict[userName.name] == 4:
        await ctx.send(f'{userName.display_name} has been kicked')
        my_dict.update({userName.name: 0})
        #await client.kick(userName)


@client.command(help='| Responds with "Sup Bitch"')
async def hello(ctx):
    await ctx.send("sup")


@client.command(help="| Checks Latency")
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')
    print(f'Ping is: {round(client.latency * 1000)}ms')


@client.command(help="| Clears inputted amount of messages or 5 by default")
# @has_permissions(administrator=True)
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
