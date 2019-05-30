import discord
import os



client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(activity=discord.Game(name="말하는 쿠키봇"))





access_token == os.environ["BOT_TOKEN"]

client.run(access_token)
