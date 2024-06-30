import discord

client = commands.Bot(description="Ello", command_prefix=prefix)

 @client.command(pass_context=True)
    async def say(ctx):
        split = client.split(" ")
        message = str(split[2])
        await client.say(message)

client.run("token")
