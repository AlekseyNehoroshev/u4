import discord
import os
import random

client = commands.Bot(description="Ello", command_prefix=prefix)

 @client.command(pass_context=True)
    async def meme1(ctx):
        images = os.listdir("images")
        r_i = random.choice(images)
        with open(f"images/{r_i}","rb") as f:
           p = discord.File(f)
        await ctx.send(file=p)

 @client.command(pass_context=True)
    async def meme2(ctx):
        images = os.listdir("images2")
        r_i = random.choice(images)
        with open(f"images/{r_i}","rb") as f:
           p = discord.File(f)
        await ctx.send(file=p)
client.run("token")
