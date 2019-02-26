import discord
from discord.ext import commands
import time
import json



owners = ['316980084634288128', '395204159416041472', '406911726638989313']

with open('secrets.json', 'r')as fp:
    bot_data = json.load(fp)

bot = commands.Bot(command_prefix=bot_data["PREFIX"])

TOKEN = bot_data["TOKEN"]

def_server = {
    "LeavandJoin" : {
        "toggled" : False,
        "whisper" : False,
        "image_url" : "https://cdn.discordapp.com/attachments/324228618375135232/499827061515616256/default.png",
        "channel" : None
        }
    }

intro = '''
Welcome and thank your for inviting Miyuki to your server :thumbsup:.

'''

@bot.event
async def on_ready():
    bot.load_extension('cogs.economy')
    bot.load_extension('cogs.shop')
    bot.load_extension('cogs.Fun')
    bot.load_extension('cogs.Moderation')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('ready to go!')

@bot.event
async def on_join(server):
    with open('Data/servers/'+server.id+'.json', 'w')as fp:
        fp.dump(def_server)
        fp.close()
        await bot.send_message(server.owner, intro)

@bot.event
async def on_leave(server):
    os.remove('Data/servers/'+server.id+'.json')
    print('kicked from '+server.name)



@bot.command(pass_context=True)
async def info(context):
    '''gives info about the bot'''
    embed = discord.Embed(title="Miyuki bot", description="Nicest bot there is ever.", color=0xeee657)
    
    #sets image
    embed.set_image(url="https://vignette.wikia.nocookie.net/yandere/images/c/c5/Sone.Miyuki.full.1565519.jpg/revision/latest?cb=20171028020605")

    # give info about you here
    embed.add_field(name="Author", value="RedSpark#8688, jdh8#1993, Jazzucci#0300")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=len(bot.servers))

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=480815207749255179&permissions=8&scope=bot")

    await bot.send_message(context.message.channel, embed=embed)

@bot.command(pass_context=True)
async def shutdown(context):
    '''shutsdown the bot'''
    if context.message.author.id in owners:
        await bot.send_message(context.message.channel, ':wave:')
        await bot.logout()
    else:
        await bot.send_message(context.message.channel, 'you are not authorised')

@bot.command(pass_context=True)
async def ping(context):
    '''pretty self explanatory'''
    before = time.monotonic()
    message = await bot.send_message(context.message.channel, "Pong!")
    ping = (time.monotonic() - before) * 1000
    print(f'Ping {int(ping)}ms')
    await bot.send_message(context.message.channel, ping)

@bot.command(pass_context=True)
async def load(context, cog):
    '''loads cog'''
    try:
        bot.load_extension('cogs.{}'.format(cog))
        await bot.send_message(context.message.channel, 'Module {} loaded'.format(cog))
    except ModuleNotFoundError:
        await bot.send_message(context.message.channel, 'Error Module {} cannot be loaded!'.format(cog))

@bot.command(pass_context=True)
async def unload(context, cog):
    '''unloads cog'''
    try:
        bot.unload_extension('cogs.{}'.format(cog))
        await bot.send_message(context.message.channel, 'Module {} unloaded'.format(cog))
    except ModuleNotFoundError:
        await bot.send_message(context.message.channel, 'Error Module {} cannot be unloaded!'.format(cog))

@bot.command(pass_context=True)
async def reload(context, cog):
    '''reloads cog'''
    try:
        bot.unload_extension('cogs.{}'.format(cog))
        bot.load_extension('cogs.{}'.format(cog))
        await bot.send_message(context.message.channel, 'Module {} reloaded'.format(cog))
    except ModuleNotFoundError:
        await bot.send_message(context.message.channel, 'Error Module {} cannot be loaded!'.format(cog))

@bot.command(pass_context=True, hidden=True)
async def status(context, nstatus):
    await bot.change_status(game=discord.Game(name=nstatus))

@bot.command(pass_context=True, hidden=False)
async def donate(context):
    '''senda a paypal donation like to keep this bot going thanks'''
    await bot.send_message(context.message.channel, 'paypal.me/ProjectQuantum')


bot.run(TOKEN)
