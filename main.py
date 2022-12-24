import discord
import os
import requests
import json
import random
from discord.ext import commands
from dislash import InteractionClient, ContextMenuInteraction

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True

#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!",intents=intents)
inter_client = InteractionClient(client)

mom_words = ["ur mom", "ur mum", "your mom", "Ur mum", "Ur mom", "Your mom", "yer mum", "yer mom", "urmom", "urmum", "Yer mum", "Yer mom", "Urmum", "Urmom"]

mom_feels = [
  "Ur mom just wants to spend time with you",
  "Ur mom thinks you can be anything you want to be",
  "Ur mom is proud of you",
  "Ur mom is grateful you exist",
  "Ur mom thinks you have great ideas",
  "Ur mom believes in you",
  "Ur mom hopes you have a great day",
  "Ur mom doesn't care how you pronounce GIF",
  "Ur mom thinks you look nice today",
  "Ur mom is happy to see you",
  "Ur mom wants you to follow your dreams",
  "Ur mom thinks you make the world a better place",
  "Ur mom thinks you don’t have to be perfect to be amazing",
  "Ur mom doesn't mind your taste in music",
  "Ur mom enjoys spending time with you",
  "Ur mom values your opinion",
  "Ur mom wants to learn more about your interests",
  "Ur mom enjoys hearing about your day",
  "Ur mom wants you to believe in yourself",
  "Ur mom forgives you",
  "Ur mom is impressed by your talents",
  "Ur mom already bought you a birthday gift",
  "Ur mom misses you",
  "Ur mom wants you to teach her how to use the Internet",
  "Ur mom is your biggest fan",
  "Ur mom thinks the book was better than the movie too",
  "Ur mom would be happy to cook your favorite dinner",
  "Ur mom saved you the last slice of cake",
  "Ur mom thinks you should definitely treat yourself",
  "Ur mom is on your side",
  "Ur mom knows you did your best",
  "Ur mom accepts who you are",
  "Ur mom admires your creativity",
  "Ur mom still has that elementary school project",
  "Seeing you happy makes ur mom happy",
  "You make ur mom a better person",
  "Ur mom thinks you're a gift to those around you",
  "Ur mom appreciates your personality",
  "You are the reason ur mom is smiling today",
  "Ur mom loves to tell everyone how amazing you are",
  "You are the apple of ur mom's eye",
  "You bring a smile to ur mom's face",
  "Giving you compliments is ur mom's favorite hobby",
  "Ur mom likes that color on you",
  "Your dance moves don't embarrass ur mom",
  "You are ur mom's favorite",
  "Ur mom is proud of how hard you work",
  "Ur mom loves listening to your stories",
  "Ur mom is astounded by your creativity",
  "Ur mom was happy to wake up with you in her family",
  "Ur mom is humbled by your generosity",
  "Ur mom loves it when you confide in her",
  "Ur mom admires how compassionate and trustworthy you are",
  "You always make your mom laugh",
  "Ur mom has every confidence in you"
]

mom_gifts = [
  "https://tenor.com/bdTRO.gif",
  "https://tenor.com/bFMLK.gif",
  "https://tenor.com/yET5.gif",
  "https://tenor.com/bgaJe.gif",
  "https://tenor.com/bkvmR.gif",
  "https://tenor.com/bu8Vr.gif",
  "https://tenor.com/FE2y.gif",
  "https://tenor.com/Urnp.gif",
  "https://tenor.com/00Zv.gif",
  "https://tenor.com/bWzhr.gif",
  "https://tenor.com/bNRcX.gif",
  "https://tenor.com/bXdaA.gif",
  "https://tenor.com/bXbTq.gif",
  "https://tenor.com/bV5Cp.gif",
  "https://tenor.com/bkO36.gif",
  "https://tenor.com/taT9.gif",
  "https://tenor.com/bmhi9.gif",
  "https://tenor.com/baWEe.gif",
  "https://tenor.com/2OU8.gif",
  "https://tenor.com/VDwQ.gif",
  "https://tenor.com/biged.gif",
  "https://tenor.com/21rI.gif",
  "https://tenor.com/bnIIU.gif",
  "https://tenor.com/bftF1.gif",
  "https://tenor.com/uLdh.gif",
  "https://tenor.com/sMMI.gif",
  "https://tenor.com/bSkat.gif",
  "https://tenor.com/bqOH4.gif",
  "https://tenor.com/bT0s1.gif",
  "https://tenor.com/bjTCy.gif",
  "https://tenor.com/bzo5S.gif",
  "https://tenor.com/7RJP.gif",
  "https://tenor.com/yHIe.gif",
  "https://tenor.com/bWM6c.gif",
  "https://tenor.com/bWobN.gif",
  "https://tenor.com/6qd1.gif",
  "https://tenor.com/blzp8.gif",
  "https://tenor.com/bGW6z.gif",
  "https://tenor.com/bbDUw.gif",
  "https://tenor.com/bUem4.gif",
  "https://tenor.com/V8fb.gif",
  "https://tenor.com/bJogI.gif",
  "https://tenor.com/7mR2.gif",
  "https://tenor.com/bUx9m.gif",
  "https://tenor.com/bjBwN.gif",
  "https://tenor.com/bcVPo.gif",
  "https://tenor.com/bcpzQ.gif",
  "https://tenor.com/byFwC.gif",
  "https://tenor.com/bxtcg.gif",
  "https://tenor.com/bvEbm.gif",
  "https://tenor.com/sGLw.gif",
  "https://tenor.com/wSij.gif",
  "https://tenor.com/1YgY.gif",
  "https://tenor.com/S5Gk.gif",
  "https://tenor.com/vV9z.gif",
  "https://tenor.com/ysrD.gif",
  "https://tenor.com/bzE9T.gif",
  "https://tenor.com/bxarN.gif",
  "https://tenor.com/bzsvV.gif"
]

@client.event

async def on_ready():
  print(f'{client.user} is connected.')


@client.event

async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
    
  if any(word in msg for word in mom_words):
    await message.channel.send(random.choice(mom_feels) + f', <@{message.author.id}>.', allowed_mentions=discord.AllowedMentions.none())


@inter_client.user_command(name="Share a Hug")
async def hug(inter: ContextMenuInteraction):
    await inter.respond(
        f"Ur Mom gave <@{inter.user.id}> a big hug."
    )

@inter_client.user_command(name="Send a Message")
async def message(inter: ContextMenuInteraction):
    await inter.respond(
        random.choice(mom_feels) + f', <@{inter.user.id}>.'
    )

@inter_client.user_command(name="Give a GIFt")
async def gift(inter: ContextMenuInteraction):
    embed=discord.Embed(color=0xFF5733)
    embed.set_image(url=random.choice(mom_gifts))
    embed.set_author(name=inter.user.display_name, icon_url=inter.user.avatar_url)
    await inter.respond(
      f"Ur Mom has a GIFt for you, <@{inter.user.id}>.",
      embed=embed
    )

client.run(TOKEN)
