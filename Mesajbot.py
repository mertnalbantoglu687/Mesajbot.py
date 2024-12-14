# Mesajbot -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import discord

import requests

import random

import time

import os

from discord.ext import commands

from Mantık import *

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix = "$",intents = intents)

print(os.listdir("Resimler"))

@bot.event
async def on_ready():
    print(f"{bot.user} Açıldı.")

@bot.command()
async def merhaba(ctx):
    await ctx.send(f"Sanada merhaba.")

@bot.command()
async def nasılsın(ctx):
    await ctx.send(f"iyiyim, sorduğun için teşekkür ederim.")

@bot.command()
async def adın(ctx):
    await ctx.send(f"Benim Adım Mesajbot.")

@bot.command()
async def ismin(ctx):
    await ctx.send(f"Benim ismim Mesajbot.")

@bot.command()
async def nerelisin(ctx):
    await ctx.send(f"Ben Discord'a aidim.")

@bot.command()
async def dinin(ctx):
    await ctx.send(f"Ben bir yapay zeka olduğum için hergangi bir dinim yok.")

@bot.command()
async def tesekkür(ctx):
    await ctx.send(f"Rica ederim her zaman yanındayım bir sorun olduğunda sormaktan çekinme.")

@bot.command()
async def parola(ctx):
    await ctx.send(Parola(25))

@bot.command()
async def kurallar(ctx):
    await ctx.send(f"PARLAK BİR GELECEK İÇİN YAPABİLECEKLERİNİZ\n\n"
    "1. Çöplerini yere değil çöp kutusuna atabilirsin.\n\n"
    "2. Geri dönüştürülebilen maddeleri çöp kutusuna değil geri dönüşüm kutusuna atabilirsin.\n\n"
    "3. En ufak tasarruftan bile kaçınmamalısın. örneğin(ellerini yıkarken suyu az açabilir\n"
    "veya gündüzleri ışıkları kapatabilirsin).\n\n"
    "4. Hava kirliliğini azaltmak amacıyla elektrikli araçlara geçiş yapabilir, toplu taşıma\n"
    "araçlarını daha sık kullanmaya özen gösterebilir, bisiklet gibi çevre dostu araçlar kullanabilir\n"
    "veya yenilenebilir enerji kaynaklarına örneğin(güneş, rüzgar, hidroelektrik) gibi kaynaklara\n"
    "yatırım yapabilirsin.\n\n"
    "5. Eğer bitki yetiştiriyorsan doğal gübreler ve kompost kullanarak toprak kirliliğini önleyebilir\n"
    "ve verimliliği arttırabilirsin.\n\n"
    "6. Gürültü kirliliğini azaltmak için araç egzoz sistemlerini düzenleyerek\n"
    "veya gürültü seviyesi düşük makineler ve ekipmanlar kullanarak ses kirliliği\n"
    "sınırlarına uyabilirsin.\n\n"
    "7. Enerji tasarrufu yapmak için yenilenebilir enerji projelerini destekleyebilir veya böyle\n"
    "projeler düzenleyebilirsiniz.\n\n"
    "8. Toprak kirliliğini azaltmak için tek kullanımlık plastik gibi atıkları kullanmayabilir\n"
    "veya daha az kullanmaya çalışabilirsin.\n\n"
    "9. Heyelan(toprak kayması) gibi doğal afetleri önlemek ve yaşam verimliliğini arttırmak amacıyla etrafı\n"
    "ağaçlandırarak yeşil alanları arttırabilirsin.\n\n"
    "10. Bunlar ve diğer çevre kirliliğini azaltma kurallarını başkalarıyla paylaşarak\n"
    "etrafındakileri bilinçlendirebilir ve çevreyle uyum içerisinde yaşamalarını sağlayabilirsin.")

@bot.command()
async def offf(ctx):
    await ctx.send(f"Belki Desen Makinesi sıkıntını giderebilir: https://hub.kodland.org/en/project/284214")

@bot.command()
async def oyun(ctx):
    await ctx.send(Oyun())

@bot.command()
async def emoji(ctx):
    await ctx.send(Surat())

@bot.command("ördek")
async def ördek(ctx):
    image_url = Ördek()
    await ctx.send(image_url)

@bot.command("köpek")
async def köpek(ctx):
    image_url = Köpek()
    await ctx.send(image_url)

@bot.command()
async def basla(ctx):
    soru = await ctx.send(f"Yazımı turamı?")
    def Cevap(mesaj):
        return mesaj.author == ctx.author and mesaj.channel == ctx.channel
    cevap_mesajı = await bot.wait_for("message", check = Cevap)
    cevap = cevap_mesajı.content.lower()
    secim = random.randint(1,2)
    if cevap == "$yazı" or cevap == "$tura":
        await ctx.send(f"Parayı atıyorum.")
        time.sleep(3)
        await ctx.send(f"Attım.")
        time.sleep(1)
    if secim == 1:
        if cevap == "$yazı" or cevap == "$tura":
            with open("Resimler/Resim1.png","rb") as f:
                picture = discord.File(f)
            await ctx.send(file = picture)
        if cevap == "$yazı":
            await ctx.send(f"Yanlış bildin.")
        elif cevap == "$tura":
            await ctx.send(f"Doğru bildin.")
        else:
            if cevap.strip():
                await ctx.send(f"Böyle bir seçenek yok.")
    elif secim == 2:
        if cevap == "$yazı" or cevap == "$tura":
            with open("Resimler/Resim2.png","rb") as f:
                picture = discord.File(f)
            await ctx.send(file = picture)
        if cevap == "$yazı":
            await ctx.send(f"Doğru bildin.")
        elif cevap == "$tura":
            await ctx.send(f"Yanlış bildin.")
        else:
            if cevap.strip():
                await ctx.send(f"Böyle bir seçenek yok.")

bot.run("")

# Mantık -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import discord

import requests

import random

def Parola(pass_length):
    karakterler = "é!'£^#+$%½&/=?\*_-@¨¨~~æß´`,;<>.:qQwWeErRtTyYuUIoOpPğĞüÜaAsSdDfFgGhHjJkKlLşŞiİzZxXcCvVbBnNmMöÖçÇ1234567890"
    sifre = ""
    for a in range(pass_length):
        sifre += random.choice(karakterler)
    return sifre

def Surat():
    emoji = ["\U0001F923","\U0001f642","\U0001f600","\U0001F606"]
    return random.choice(emoji)

def Oyun():
    secim = ["https://hub.kodland.org/en/project/289819","https://hub.kodland.org/en/project/308651","https://hub.kodland.org/en/project/296170"]
    return random.choice(secim)

def Ördek():    
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data["url"]

def Köpek():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data["url"]
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
