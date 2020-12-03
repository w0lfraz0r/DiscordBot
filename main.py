import discord
import datetime
# from goto import goto, comefrom, label
import time as t
from discord.ext import commands as commands
from ruamel.yaml import YAML
import os
import webscrap as w
# our user defined module

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
    
    # label .myLabel
    game_info = w.find_game() #returns list containg name and url of the game
    today = t.localtime(t.time())
    print("reached here 1")
    if today.tm_mday == 3:
        if today.tm_hour >= 21 and today.tm_min>35:
            print("reached here 2")
            
            await bot.log_channel.send(channel=log_channel_id,content="Here is your free Game\n Name : {}\nPlease Click here : {}".format(game_info[0],game_info[1]))
        else:
            print("reached here 3")
            # sleep for 1 hr
            await bot.log_channel.send(channel=log_channel_id,content="Here is your free Game\n Name : {}\nPlease Click here : {}".format(game_info[0],game_info[1]))
            t.sleep(3600)
            # goto .mylable
    else :
        print("reached here 2")
        t.sleep(86400) #1 day
        # goto .mylable 
    

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