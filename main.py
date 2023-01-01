import discord
import os
import requests
import json
import random
from discord.ext import commands
from dislash import InteractionClient, ContextMenuInteraction, Option, OptionType

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True

#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)
inter_client = InteractionClient(client)


mom_words = ["ur mom", "ur mum", "your mom", "yer mum", "yer mom", "urmom", "urmum", "joe mama"]

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
  "https://media.tenor.com/FvUf1z5-3C0AAAAC/mamma-loves-you-bear.gif",
  "https://media.tenor.com/nQayoDoOxwwAAAAd/big-hug.gif",
  "https://media.tenor.com/M9-IjlV8PvAAAAAC/cat-kitten.gif",
  "https://media.tenor.com/zztSFhzHjrEAAAAC/proud-momma-ugly-duckling.gif",
  "https://media.tenor.com/q3xb9dTcsO4AAAAd/proud-this-mama-is-so-proud.gif",
  "https://media.tenor.com/EIXLW2Mr5_4AAAAC/mulan-mushu.gif",
  "https://media.tenor.com/NizRmlvwDuQAAAAC/my-baby-proud.gif",
  "https://media.tenor.com/rNaVahgq2-sAAAAC/who-loves-you-me.gif",
  "https://media.tenor.com/l8H5SZtJpn8AAAAC/baby-groot-groot.gif",
  "https://media.tenor.com/RD-BXcI_XmoAAAAC/friends.gif",
  "https://media.tenor.com/MyH51fMIUcgAAAAC/love.gif",
  "https://media.tenor.com/eHWFMSY8OKEAAAAC/cat-cat-cute.gif",
  "https://media.tenor.com/aSu9j8A_eDgAAAAC/love-heart.gif",
  "https://media.tenor.com/bvlcqExA9HcAAAAC/winnie-the-pooh-hug.gif",
  "https://media.tenor.com/F4T2XLGkYrsAAAAC/baby-pooh-disney.gif",
  "https://media.tenor.com/8qtOK6_iNRMAAAAC/proud-ron-swanson.gif",
  "https://media.tenor.com/rDLiZ5a12EUAAAAC/iam-so-proud-of-you-proud.gif",
  "https://media.tenor.com/gSat6H4E_9EAAAAd/thank-you-touched.gif",
  "https://media.tenor.com/5giHBBghUrIAAAAd/proud-of-you-thumbs-up.gif",
  "https://media.tenor.com/rQ0aO6TStkwAAAAd/good-job-clapping.gif",
  "https://media.tenor.com/xMA8DDd6NxYAAAAC/fabulous-clapping.gif",
  "https://media.tenor.com/mOTMdcVdJScAAAAC/favorite-person-youre-my-favorite-person.gif",
  "https://media.tenor.com/Nl7-iFy56-EAAAAC/shim-cute.gif",
  "https://media.tenor.com/84O6Tg6gO3UAAAAd/youre-like-the-best-part-of-my-day-happy.gif",
  "https://media.tenor.com/QOfETzVbUIcAAAAC/2broke-girls-kat-dennings.gif",
  "https://media.tenor.com/FWQbOVWe_AgAAAAC/favorite-human-fave.gif",
  "https://media.tenor.com/YKKwio0xvwAAAAAd/twitch-widowontwitch.gif",
  "https://media.tenor.com/TTK6TYJwv7QAAAAC/youre-the-best-person-i-know-violet-valentine.gif",
  "https://media.tenor.com/eMKHTR5iKdsAAAAC/you-are-the-most-extraordinary-person-i-know-raffi-musiker.gif",
  "https://media.tenor.com/TfbLnEL_Fm4AAAAC/yoda-baby-yoda.gif",
  "https://media.tenor.com/h13TEmmSgIcAAAAd/good-morning.gif",
  "https://media.tenor.com/1TvWvdCPwKIAAAAC/snow-white-snow-white-and-the-seven-dwarfs.gif",
  "https://media.tenor.com/jWKliGgKsIUAAAAC/hug-love.gif",
  "https://media.tenor.com/h9222Kcym9MAAAAd/cat-bagel.gif",
  "https://media.tenor.com/3lUsJXIwCogAAAAC/cat-love.gif",
  "https://media.tenor.com/YEKkoT3qY9UAAAAC/cat-love.gif",
  "https://media.tenor.com/GSahnDhnNFEAAAAC/virtual-hug-hugs.gif",
  "https://media.tenor.com/-13Xmg8Gd6wAAAAC/hug.gif",
  "https://media.tenor.com/Dwrij1L3z_0AAAAC/gnome-knitting-gnome.gif",
  "https://media.tenor.com/fsItygHEVvIAAAAC/sending-love.gif",
  "https://media.tenor.com/bqpJeuiZ990AAAAd/positivity-beat.gif",
  "https://media.tenor.com/Ez5abQcBMJIAAAAC/loveyou-kiss.gif",
  "https://media.tenor.com/_bLN46BQbPsAAAAC/sending-love-love.gif",
  "https://media.tenor.com/PCAMETJ5uiAAAAAC/animated-text.gif",
  "https://media.tenor.com/xDw134Byz4QAAAAC/animal-crossing-balloon.gif",
  "https://media.tenor.com/3hCSZTd1OIQAAAAC/bunny-love.gif",
  "https://media.tenor.com/IttyNslATd8AAAAC/simply-the-best-tina-turner.gif",
  "https://media.tenor.com/z8bHk65eOQEAAAAC/loveumore-loveyou.gif",
  "https://media.tenor.com/z_WREcsJQPIAAAAd/i-just-think-youre-so-amazing-claire-harper.gif",
  "https://media.tenor.com/BJdhWOdKRJ4AAAAd/you-are-the-best-tracey-matney.gif",
  "https://media.tenor.com/wpXFWSyd7aEAAAAC/tenor.gif",
  "https://media.tenor.com/4mravgPkF6gAAAAC/wonderful-parks-and-recreation.gif",
  "https://media.tenor.com/RtqyBgRy0pIAAAAC/amy-poehler-thumbs-up.gif",
  "https://media.tenor.com/2VTq0Gu_Y5oAAAAC/chris-traeger-rob-lowe.gif",
  "https://media.tenor.com/IPq0GAt1PykAAAAC/parcs-and-rec-craig.gif",
  "https://media.tenor.com/0y7SMmD7CFUAAAAC/leslie-knope-best-friends.gif",
  "https://media.tenor.com/WjPIwKWEABMAAAAC/youre-a-good-person-dan-levy.gif",
  "https://media.tenor.com/yVsytwch5bcAAAAd/radiant-catherine-o-hara.gif",
  "https://media.tenor.com/MXFKcqlBX2MAAAAC/go-you-annie-murphy.gif",
  "https://media.tenor.com/hTY9Iv-tto0AAAAC/love-valentines-day.gif",
  "https://media.tenor.com/ipwf7f9kN_AAAAAC/bear-affirmation.gif",
  "https://media.tenor.com/CNkkeroB26AAAAAd/you-are-amazing-alesha-dixon.gif",
  "https://media.tenor.com/dumQlZBqaF8AAAAC/awesome-motivate.gif",
  "https://media.tenor.com/PIlYlq4_kIkAAAAC/hello-friends-music-on.gif",
  "https://media.tenor.com/VTGY2jOoGMMAAAAd/you-are-amazing-you-are-phenomenal.gif",
  "https://media.tenor.com/XeszZ1AfFgoAAAAd/youre-a-wonderful-human-youre-a-great-person.gif",
  "https://media.tenor.com/QeHZnrB3s68AAAAC/the-great-gatsby-compliment.gif",
  "https://media.tenor.com/cBPJ2H-LP_QAAAAd/youre-just-beautiful-people-mike.gif",
  "https://media.tenor.com/6F8DcJ1hvTAAAAAM/baby-groot-dancing.gif",
  "https://media.tenor.com/XL-0Ipg8c-4AAAAM/sandeepkvk18.gif",
  "https://media.tenor.com/7Mn2btwwvJUAAAAC/i-love-you-you-are-wonderful-americas-got-talent.gif",
  "https://media.tenor.com/Ov_EVhUq4KAAAAAC/transformers-bumblebee.gif",
  "https://media.tenor.com/d9h4w4roPEIAAAAC/positive-glitter.gif",
  "https://media.tenor.com/U6desJj5J54AAAAC/fabulous-you-are-a-fabulous-wonderful-individual.gif",
  "https://media.tenor.com/vcQm8_mrwUQAAAAd/youre-special-saturday-night-live.gif",
  "https://media.tenor.com/TeuG1ufhm10AAAAd/i-love-you-beautiful.gif",
  "https://media.tenor.com/S2d4Qfi62_YAAAAC/self-awareness-you-deserve-love.gif",
  "https://media.tenor.com/9V_FuwXJyd8AAAAC/loof-and-timmy-loof.gif",
  "https://media.tenor.com/vcirp4UZjVQAAAAC/i-love-you.gif",
  "https://media.tenor.com/p7MW46WjVWsAAAAC/cute-bird.gif",
  "https://media.tenor.com/02u09QzFXmkAAAAC/you-are-loved-gifkaro.gif",
  "https://media.tenor.com/PsjB4BIb4PsAAAAC/headphones-taylorswift.gif",
  "https://media.tenor.com/6Qqzg9RuX2wAAAAC/mister-rogers-celebration.gif",
  "https://media.tenor.com/GBXlekv-BpgAAAAC/mr-rogers-just-the-way-you-are.gif",
  "https://media.tenor.com/USrolH4hGUYAAAAC/beautiful-piece-of-pizza.gif",
  "https://media.tenor.com/f_UJlEeY3GAAAAAC/taylor-swift-thanks.gif",
  "https://media.tenor.com/IUDBHGmQHRAAAAAC/gif.gif"
]

@client.event

async def on_ready():
  print(f'{client.user} is connected.')


@client.event

async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content.lower()
    
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
    embed=discord.Embed()
    embed.set_image(url=random.choice(mom_gifts))
   #embed.set_author(name=inter.user.display_name, icon_url=inter.user.avatar_url)
    await inter.respond(
      f"Ur Mom has a GIFt for you, <@{inter.user.id}>.",
      embed=embed
    )

@inter_client.message_command(name="Reply With a Hug")
async def hug_reply(inter: ContextMenuInteraction, message: discord.Message):
    if inter.message.content:
      await inter.message.reply(
          f"Ur Mom gave <@{inter.message.author.id}> a big hug."
      )
      await inter.respond("Hug has been sent!")

@inter_client.message_command(name="Reply With a Message")
async def message_reply(inter: ContextMenuInteraction):
    if inter.message.content:
      await inter.respond(
          random.choice(mom_feels) + f', <@{inter.message.author.id}>.'
      )

@inter_client.message_command(name="Reply With a GIFt")
async def gift_reply(inter: ContextMenuInteraction):
    embed=discord.Embed()
    embed.set_image(url=random.choice(mom_gifts))
   #embed.set_author(name=inter.user.display_name, icon_url=inter.user.avatar_url)
    if inter.message.content:
      await inter.respond(
        f"Ur Mom has a GIFt for you, <@{inter.message.author.id}>.",
        embed=embed
      )

@inter_client.slash_command(
  description="Share a hug from Ur Mom",
  options=[
      Option("user", "Enter the user", OptionType.USER, required=True)
  ]
)

async def share_hug(inter, user=None):
    user = user or inter.author
    await inter.reply(
      f"Ur Mom gave <@{user.id}> a big hug."
    )

@inter_client.slash_command(
  description="Send a message from Ur Mom",
  options=[
      Option("user", "Enter the user", OptionType.USER, required=True)
  ]
)

async def send_message(inter, user=None):
    user = user or inter.author
    await inter.reply(
      random.choice(mom_feels) + f', <@{user.id}>.'
    )

@inter_client.slash_command(
  description="Give a GIFt from Ur Mom",
  options=[
      Option("user", "Enter the user", OptionType.USER, required=True)
  ]
)

async def give_gift(inter, user=None):
    user = user or inter.author
    embed=discord.Embed()
    embed.set_image(url=random.choice(mom_gifts))
    await inter.reply(
      f"Ur Mom has a GIFt for you, <@{user.id}>.",
      embed=embed
    )

client.run(TOKEN)


