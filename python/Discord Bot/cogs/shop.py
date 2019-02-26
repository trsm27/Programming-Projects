import discord
from discord.ext import commands
import json

sale = {
    "tent": 200,
    "backpack": 150,
    "broadSword": 50,
    "shield": 20
}

def_inv = {"items":["magnets"]}

class shop:
    """A way to wste your in-bot currency!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def make_inventory(self, context):
        """preps your inventory for the market!"""
        try:
            with open('Data/shop/'+context.message.author.id+'.json', 'r')as fp:
                await self.bot.send_message(context.message.channel, 'you already have an inventory!')
                fp.close()
        except FileNotFoundError:
            with open('Data/shop/'+context.message.author.id+'.json', 'w')as fp:
                json.dump(def_inv, fp)
                fp.close()
                await self.bot.send_message(context.message.channel, 'your inventory has been created!')
    
    @commands.command(pass_context=True)
    async def inventory(self, context):
        '''check your inventory'''
        try:
            with open('Data/shop/'+context.message.author.id+'.json', 'r')as fp:
                inv = json.load(fp)
                fp.close()
                for x in range(len(inv["items"])):
                    print (inv["items"][x])
                    await self.bot.send_message(context.message.channel, inv["items"][x])
        except FileNotFoundError:
            await self.bot.send_message(context.message.channel, 'you have not set up your inventory use m.make_inventory')
    
    @commands.command(pass_context=True)
    async def buy(self, context, item):
        '''buy things for your inventory'''
        try:
            user = context.message.author.id
            with open('Data/economy/'+user+'.json', 'r') as fp:
                parsed_json = json.load(fp)
                prev_moneyz = int(parsed_json[user])
                new_moneyz = prev_moneyz-int(sale[item])
                if new_moneyz > 0 or new_moneyz == 0:
                    new_usr = {user: new_moneyz}
                    with open('Data/shop/'+user+'.json', 'r')as fp:
                        inventory = json.load(fp)
                        fp.close()
                        inventory["items"].append(item)

                    with open('Data/shop/'+user+'.json', 'w')as fp:
                        json.dump(inventory, fp)
                        fp.close()
                        await self.bot.send_message(context.message.channel, 'your balance now is {}:yen:'.format(new_moneyz))

                else:
                    await self.bot.send_message(context.message.channel, "you do not have enough :yen:!")
                    new_usr = {user: prev_moneyz}
                

            with open('Data/economy/'+user+'.json', 'w') as fp:
                json.dump(new_usr, fp)
                fp.close()
        except FileNotFoundError:
            await self.bot.send_message(context.message.channel, 'You don\'t have an account yet\n make one by typing m.register!' )



def setup(bot):
    bot.add_cog(shop(bot))
