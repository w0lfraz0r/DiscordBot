import discord
from discord.ext import commands as commands

bot = commands.Bot(command_prefix="$",description="my description  blah blah",case_insensitive =True)
753919284849410061

@bot.event
async def on_ready():
    print("I am connected to Discord.")
    channel = bot.get_channel(753919284849410061)
    await channel.send(content ="I am online")
    channel.send(content ="Here is your free game - https://www.epicgames.com/store/en-US/free-games ")


bot.run("NzY2MTc3MTk3NjY3OTA5NjYy.X4fkHg.7RPmPCpsxfzD32PIesBVZ3UctQ8", bot = True,reconnect=True)
