
import discord 
import requests
from discord.ext import commands 
from discord import member
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from apikeys import *
import json
import os

intents = discord.Intents.default()
intents.members=True 
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
#client = commands.Bot(command_prefix="!", intents=intents)
@client.event 
async def on_ready():
    print("the bot is moist")
    print("--------------------------")

@client.command()
async def hello(ctx):
    print("fuck")
    await ctx.send("hello , im big d randy")
@client.event
async def on_member_join(member):
    print("hello")
    jokeurl = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
	    "X-RapidAPI-Key": rapidApikey,
	    "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
        }

    response = requests.get(jokeurl, headers=headers)
    print(response.json())
    joke=response.json()
    joke=joke["body"][0]["setup"]+joke["body"][0]["punchline"]
    channel= client.get_channel(1121961682432954471)
    await channel.send("randy says hello")
    await channel.send(joke)

    #await member.send("im coming for u candy")
@client.event
async def on_member_remove(member):
    print("hello3")
    channel= client.get_channel(1121961682432954471)
    await channel.send("randy says u aint leaving with that booty ")

@client.command(pass_context= True)
async def join(ctx):
    if ctx.author.voice:
        channel=ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("get in voice channel for randy to join")
@client.command(pass_context= True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("randy had his booty and left the voice channel")
    else:
        await ctx.send("randy isnt in no smelly voice channel")
@client.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages sent by bots
    print(message)
    print("---")
    print(message.content)
    if message.content=="randy":
        await message.delete()
        await message.channel.send("dont mention the lords name in vain ")
        # await message.author.kick(reason=None)
    await client.process_commands(message)


@client.command()
async def kick(ctx, member:discord.Member, *,reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked.')
    else:
        await ctx.send("you dont have powers bitch")


# @client.command()
# async def ban(ctx, member:discord.Member, *,reason=None):
#     if ctx.author.guild_permissions.ban_members:
#         await member.ban(reason=reason)
#         await ctx.send(f'User {member} has been banned.')
#     else:
#         await ctx.send("Insufficient permissions, requires `BAN_MEMBERS` permission.")

client.run(bottoken)