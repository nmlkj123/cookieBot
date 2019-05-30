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





client.run('NTgyNzc3MzU0NjIzOTA5ODk4.XOywRA.-rbxJkijR2Lvhe30Kh2JQKH4n48')
