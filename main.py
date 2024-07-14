import discord
import random
from discord.ext import commands
description = 'g'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.command(name='commands')
async def _bot(ctx):
    await ctx.send('1.подделки из пластиклвых бутылок')
    await ctx.send('2.самые загрязненные места(информация)')

@bot.command(name='1')
async def _bot(ctx):
	await ctx.send('видео для идей из пластиковых бутылок: https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DRlERRK0Aea8&ved=2ahUKEwiKtMbnhaaHAxUDUqQEHcTACNMQwqsBegQIFhAF&usg=AOvVaw3g7UWQfYJiFa2tB-AP0oXt')

@bot.command(name='2')
async def _bot(ctx):
	await ctx.send(random.chooise('https://www.google.com/amp/s/www.kommersant.ru/amp/4548601', 'https://www.rbc.ru/society/05/06/2019/5cf74b8c9a79471aab7e6281','https://www.meteovesti.ru/news/1680864930747-nazvany-goroda-rossii-s-samym-gryaznym-vozduhom'))
	
bot.run('token')
