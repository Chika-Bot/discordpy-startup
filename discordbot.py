import time
from discord.ext import commands
from cogs import evals
import os
import random
import traceback
import discord
import time
import datetime
import requests
import psutil

bot = commands.Bot(command_prefix='#.')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="#.help|仮運用中"))
    evals.setup(bot)
    print("logged in as " + bot.user.name)
    for channel in bot.get_all_channels():
        if channel.name == 'しゅーBot起動時メッセージ':
            await channel.send('おはようございます！\n今日も頑張りましょう！')

@bot.command()
async def help(ctx):
    await ctx.send('準備中です。')
            
@bot.command()
async def cmd-test(ctx):
    await ctx.send('コマンドは受理されています。')
    
@bot.command()
async def ペテルギウス(ctx):
    await ctx.send('あなた、怠惰ですね?')    

@client.event
async def on_message(message):
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('本当に消して.....よかったの?')
        else:
            await message.channel.send('なんであなたがコメント消すの...?もうちょっと考えてみようか?')

@bot.command(name="プレイ中変更")
# @commands.is_owner()
async def pureityuudadada(ctx, *, st):
    if ctx.message.author.id == 623092854083813376:  # このidのとこは自身のIDに変更してね
        await bot.change_presence(activity=discord.Game(name=st))
        await ctx.send(embed=discord.Embed(title="変更しました！", description=f"{st}"))
    else:
        await ctx.send(embed=discord.Embed(title="あなたは違いますよ！？", description="何しているんですか！？"))
            
 
            
bot.run(token)
