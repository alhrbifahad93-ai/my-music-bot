import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

# إعدادات البوت الأساسية
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# 1. حط هنا أيدي الروم الصوتي حقك (بدل الأصفار)
VOICE_CHANNEL_ID = 1423404186761953463 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # البوت يدخل الروم تلقائياً أول ما يشتغل
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel:
        await channel.connect()

@bot.command()
async def play(ctx, url):
    if not ctx.voice_client:
        await ctx.author.voice.channel.connect()
    # لتشغيل روابط مباشرة (مثل راديو أو mp3)
    source = await discord.FFmpegOpusAudio.from_probe(url)
    ctx.voice_client.play(source)

keep_alive()
# 2. حط التوكن حقك هنا بين القوسين
# بدلاً من bot.run("TOKEN") العادي
bot.run("MTQ3ODgwMTEwMDg2NTAxNTgzOA.GMDAtA.M-TARbqgP5VfGrYlVL-60DA0xzQLlq2q9StXJk")
