import discord
from discord.ext import commands

class Moderation:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def mkick(self, context, userName: discord.User):
        """Only the server Owner can do this!"""
        #Your code will go here
        if context.messahe.server.Owner.id == context.message.author.id:
            await self.bot.send_message(userName, 'Your have been kicked from this server by {}'.format(context.message.author.name))
            await self.bot.kick(userName)
        else:
            await self.bot.send_message(context.message.channel, 'you are not the server owner!')
        
    @commands.command(pass_context=True)
    async def mban(self, context, userName: discord.User):
        """Only the server Owner can do this!"""
        #Your code will go here
        if context.message.server.Owner.id == context.message.author.id:
            await self.bot.send_message(userName, 'Your have been banned from this server by {}'.format(context.message.author.name))
            await self.bot.ban(userName)
        else:
            await self.bot.send_message(context.message.channel, 'you are not the server owner!')


def setup(bot):
    bot.add_cog(Moderation(bot))
