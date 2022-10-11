import discord
import os
import discord.ext
import threading
import datetime
import time
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check

client = discord.Client()

client = commands.Bot(command_prefix = '!')

@client.command()
async def ping(ctx):
    '''Returns the bot latency from the server, in milliseconds.'''
    if ctx.author.permissions_in(ctx.channel).manage_messages == False:
        await ctx.send("Insufficient permissions.")
        return
    import datetime
    elapsedtime = datetime.datetime.now() - ctx.message.created_at
    await ctx.send(":ping_pong: Pong! " + str(elapsedtime.microseconds/1000) + " ms") #simple command so that when you type "!ping" the bot will respond with "pong!"

@client.command()
async def role(ctx, requestedrole):
    codingroleid = 1028887935543685191
    # ----- TEST SERVER ----- codingroleid = 1029191464888057906
    fundraisingroleid = 1028888064388505690
    # ----- TEST SERVER ----- fundraisingroleid = 1029191716361748531
    if requestedrole.lower() == "coding":
        await ctx.author.add_roles(ctx.guild.get_role(int(codingroleid)))
        await ctx.send(":white_check_mark: `Coding Team` role successfully given!")
    elif requestedrole.lower() == "fundraising":
        await ctx.author.add_roles(ctx.guild.get_role(int(fundraisingroleid)))
        await ctx.send(":white_check_mark: `Fundraising Team` role successfully given!")
    else:
        await ctx.send("`" + requestedrole + "` is not a valid role. Try typing `!role coding` or `!role fundraising` instead.")


@role.error
async def command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You need to provide a specific role. Try `!role coding` or `!role fundraising` instead.")
