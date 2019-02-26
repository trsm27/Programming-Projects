import discord
from discord.ext import commands
import random
import json

Default_bank_account = {
    "BALANCE" : 0
    }

def check_user(user):
    try:
        with open('Data/economy/'+user+'.json', 'r')as test:
            return True
    except FileNotFoundError:
        return False

def get_balance(user):
    try:
        with open('Data/economy/'+user+'.json', 'r')as fp:
            cache = json.loads(fp)
            balance = cache["balance"]
            fp.close()
    except FileNotFoundError:
        balance = "You do not have an account"


class Economy:
    """In-bot currency!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def balance(self, context):
        """gives you money(spoiler alert it has a cooldown function)!"""
        try:
            with open('Data/economy/'+context.message.author.id+'.json', 'r')as fp:
                parsed_json = json.load(fp)
                monez = parsed_json[context.message.author.id]
                await self.bot.send_message(context.message.channel, 'your balance is {}:yen:'.format(monez))
                fp.close()
        except FileNotFoundError:
            await self.bot.send_message(context.message.channel, 'you have not created an account\nmake one by using m.register!')
    
    @commands.command(pass_context=True)
    async def payout(self, context):
        try:
            user = context.message.author.id
            with open('Data/economy/'+user+'.json', 'r') as fp:
                parsed_json = json.load(fp)
                prev_moneyz = int(parsed_json[user])
                new_moneyz = prev_moneyz+int('100')
                new_usr = {user: new_moneyz}
                

            with open('Data/economy/'+user+'.json', 'w') as fp:
                json.dump(new_usr, fp)
                fp.close()
                await self.bot.send_message(context.message.channel, 'your balance now is {}:yen:'.format(new_moneyz))
        except FileNotFoundError:
            await self.bot.send_message(context.message.channel, 'You don\'t have an account yet\n make one by typing m.register!' )
    
    @commands.command(pass_context=True)
    async def register(self, context):
        try:
            with open('Data/economy/'+context.message.author.id+'.json', 'r')as fp:
                fp.close()
                await self.bot.send_message(context.message.channel, 'You already have an account!')
        except FileNotFoundError:
            text = {
                context.message.author.id: 0,
                "level": 0
            }
            with open('Data/economy/'+context.message.author.id+'.json', 'a')as fp:
                fp.write(json.dumps(text))
                fp.close()
            
            await self.bot.send_message(context.message.channel, 'Account opened!')

def setup(bot):
    bot.add_cog(Economy(bot))
