import discord
from discord.ext import commands
import os 
import random 
import requests
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
async def mem(ctx):
    with open('', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
@bot.command()
async def kedy(ctx):
    ImageName = random.choice(os.listdir("C:\\Users\\burak\.vscode\\ders5\\resimler"))
    with open(f'C:\\Users\\burak\.vscode\\ders5\\resimler/{ImageName}','rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('diz')
async def diz(ctx):
    ImageName = random.choice(os.listdir("C:\\Users\\burak\.vscode\\ders5\\resimler2"))
    with open(f'C:\\Users\\burak\.vscode\\ders5\\resimler2/{ImageName}','rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("")
