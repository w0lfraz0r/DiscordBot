import discord
import datetime
from discord.ext import commands as commands
from ruamel.yaml import YAML
import os

yaml = YAML()

with open("./Config.yml", "r", encoding = "utf-8") as file:
    config = yaml.load(file)


bot = commands.Bot(command_prefix=config['Prefix'],description="my description  blah blah",case_insensitive =True)


log_channel_id = config['Log Channel ID']


##values for embed that do not change
bot.embed_color = discord.Color.from_rgb(
    config['Embed Settings']['Color']['r'],
    config['Embed Settings']['Color']['g'],
    config['Embed Settings']['Color']['b']
    )
bot.footer = config['Embed Settings']['Footer']['Text']
bot.footer_image = config['Embed Settings']['Footer']['Icon URL']
bot.prefix = config['Prefix']
bot.playing_status = config['Playing Status'].format(prefix = bot.prefix)

bot.TOKEN = os.getenv(config['Bot Token Variable Name'])

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} and connected to Discord! (ID: {bot.user.id})")
    
    game =discord.Game(name= bot.playing_status)
    await bot.change_presence(activity =game)

    embed = discord.Embed(
        title = f"{bot.user.name} Online!",
        color = bot.embed_color,
        timestamp = datetime.datetime.utcnow()
    )
    embed.set_footer(
        text = bot.footer,
        icon_url = bot.footer_image
    )

    bot.log_channel = bot.get_channel(log_channel_id)
    await bot.log_channel.send(embed=embed)
    #await log_channel.send(content ="Here is your free game - https://www.epicgames.com/store/en-US/free-games ")


@bot.command(name ="restart", aliases=["r"], help="Restart the bot")
async def restart(ctx):
    embed = discord.Embed(
        title = f"{bot.user.name} Restarting!",
        color = bot.embed_color,
        timestamp = datetime.datetime.utcnow()
    )
    embed.set_author(
        name = ctx.author.name,
        icon_url =ctx.author.avatar_url
    )
    embed.set_footer(
        text = bot.footer,
        icon_url = bot.footer_image
    )
    await bot.log_channel.send(embed =embed)
    await ctx.message.add_reaction('👍')
    await bot.close()


##run the bot
bot.run(bot.TOKEN)