import discord
from discord.ext import commands

import random 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def yardım(ctx):
    await ctx.send(f'hangi konuda')

@bot.command()
async def çevre_kirliliği(ctx):
    await ctx.send(f'çevreye karşı daha dikkatli olmalısın yada çevreye zarar vermicek ürünler kullanmalısın')

@bot.command()
async def başka_çözümleri_var_mı(ctx):
    await ctx.send(f'çevre kirliliği konusuyla ilgilenen bir derneğe bağış yapabilir yada çevrendeki kişilere çevrelerine dikkatli olmasını söyleyebilirsin')

bot.run('')
 
