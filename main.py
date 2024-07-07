import discord
import os
import random

client = commands.Bot(description="Ello", command_prefix=prefix)

 @client.command(pass_context=True)
    async def say(ctx):
        images = os.listdir("images")
        r_i = random.choice(images)
        with open(f"images/{r_i}","rb") as f:
           p = discord.File(f)
        await ctx.send(file=p)

client.run("token")
