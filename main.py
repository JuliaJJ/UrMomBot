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


@inter_client.user_command(name="Give a Hug")
async def hug(inter: ContextMenuInteraction):
    await inter.respond(
        f"Ur Mom gave <@{inter.user.id}> a big hug."
    )

@inter_client.user_command(name="Send a Message")
async def message(inter: ContextMenuInteraction):
    await inter.respond(
        random.choice(mom_feels) + f', <@{inter.user.id}>.'
    )

client.run(TOKEN)
