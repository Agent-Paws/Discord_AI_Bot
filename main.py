# bot.py
import math
import os
import io
import random
import csv
import discord
import datetime
import chatbot_framework

from discord import opus
from discord.ext.commands import Bot, has_permissions, CheckFailure, MissingPermissions
from discord.ext import commands
from threading import Timer
import time
from dotenv import load_dotenv
from collections import namedtuple

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='~')


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
                    # print(chatbot_framework.context(question))
                    pass


# COMMANDS

kick_dict = {'username': 'counter'}
voted_dict = {'username': 'voted for'}
@client.command(pass_context=True)
async def votekick(ctx, userName: discord.User):
    member = ctx.me
    voter = ctx.message.author.name
    if voter not in voted_dict: #check if user has voted before or not, if not then add him to voted tuple
        voted_dict.update({voter: 'user'})

    if str(voted_dict[voter]) == str(userName.name): #check if the user has voted for the same user before
        await ctx.send("You have already voted!")
    else: #add the vote
        if userName.name not in kick_dict:
            kick_dict.update({userName.name: 1})
            voted_dict.update({voter: userName.name})
        else:
            kick_dict[userName.name] += 1
        await ctx.send(f'{kick_dict[userName.name]}/4 people have voted to kick {userName.display_name}')

    if kick_dict[userName.name] == 4: ##once reaches limit, kicks user
        await ctx.send(f'{userName.display_name} has been kicked')
        kick_dict.update({userName.name: 0})
        #await discord.Guild.kick(member.guild, userName)

mute_dict = {'username': 'counter'}
mvoted_dict = {'username': 'voted for'}
@client.command(pass_context=True)
async def votemute(ctx, userName: discord.Member):
    voter = ctx.message.author.name
    member = ctx.me
    if voter not in mvoted_dict:
        mvoted_dict.update({voter: 'user'})

    if str(mvoted_dict[voter]) != str(userName.name):
        if userName.name not in mute_dict:
            mute_dict.update({userName.name: 1})
            mvoted_dict.update({voter: userName.name})
        else:
            mute_dict[userName.name] += 1
        await ctx.send(f'{mute_dict[userName.name]}/4 people have voted to mute {userName.display_name}')
    else:
        await ctx.send("You have already voted!")

    if mute_dict[userName.name] == 4:
        mute_dict.update({userName.name: 0})
        server = member.guild
        role = server.get_role(825795491287138324)
        await userName.add_roles(role)
        embed = discord.Embed(title="User Muted!",
                              description="**{0}** was muted by **{1}**!".format(member, ctx.message.author),
                              color=0xff00f6)
        await ctx.send(embed=embed)
        time.sleep(60)
        await userName.remove_roles(role)


@client.command(pass_context=True)
async def unmute(ctx, userName: discord.Member):
    member = ctx.me
    server = member.guild
    role = server.get_role(825795491287138324)
    await userName.remove_roles(role)


@has_permissions(administrator=True)
@client.command(pass_context=True)
async def mute(ctx, userName: discord.Member):
    member = ctx.me
    server = member.guild
    role = server.get_role(825795491287138324)
    await userName.add_roles(role)


@client.command(pass_context=True)
async def nostalgia(ctx):
    server = ctx.guild
    channel = ctx.channel
    answer_list = []

    if channel.name == 'nostalgia':
        with open('data/responses_csv/Text/nostalgia.csv', 'r', encoding="utf-8") as file:
            reader = csv.reader(file)
            k = 0
            for row in reader:
                answer_list.insert(k, row)
                k += 1
        random.shuffle(answer_list)
        i = 0
        for word in answer_list:
            i += 1
            word = ''.join(map(str, word))
            word = word.replace("{", "").replace("}", "")
            await ctx.send(word)
        await ctx.send("done")
    else:
        await ctx.send("wrong channel dumbass")


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
        await ctx.channel.purge(limit=amount + 1)
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
