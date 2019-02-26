import discord
from discord.ext import commands
import random

class Fun:
    """its kinda in the name of the cog ya know"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def punch(self, context, user : discord.Member):
        """Punch someone in the face!"""
        await self.bot.say("<@{}> punched {}!".format(context.message.author.id, user.mention))
        punch_file = random.choice(["Data/Fun/1.gif", "Data/Fun/2.gif", "Data/Fun/3.gif"])
        with open(punch_file, 'rb')as fp:
            await self.bot.send_file(context.message.channel, fp)

    @commands.command(pass_context=True)
    async def slap(self, context, user : discord.Member):
        """Slap someone in the face!"""
        await self.bot.say("<@{}> slapped {}!".format(context.message.author.id, user.mention))
        punch_file = random.choice(["Data/Fun/4.gif", "Data/Fun/5.gif", "Data/Fun/6.gif"])
        with open(punch_file, 'rb')as fp:
            await self.bot.send_file(context.message.channel, fp)

    @commands.command(pass_context=True)
    async def kick(self, context, user : discord.Member):
        """kick someone!"""
        await self.bot.say("<@{}> kicked {}!".format(context.message.author.id, user.mention))
        punch_file = random.choice(["Data/Fun/7.gif", "Data/Fun/8.gif", "Data/Fun/9.gif"])
        with open(punch_file, 'rb')as fp:
            await self.bot.send_file(context.message.channel, fp)

def setup(bot):
    bot.add_cog(Fun(bot))
