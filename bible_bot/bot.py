import os
import discord
import requests
from time import sleep
from profanity_filter import ProfanityFilter
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('GENERAL_CHANNEL')

pf = ProfanityFilter()
client = discord.Client()


@client.event
async def on_ready():
    guild = ""
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print('Logged in as')
    print("Client Name: " + client.user.name)
    print("Client ID: " + str(client.user.id))
    print("Guild Name: " + guild.name)
    print("Guild ID: " + str(guild.id))
    print("Default Channel: " + str(CHANNEL))
    get_verse()
    print('-' * 20)


@client.event
async def on_message(message):
    user = message.author.display_name
    pf.censor_char = "*"
    pf.custom_profane_word_dictionaries = {'en': {'caden', 'justin'}}
    clean = pf.is_clean(message.content)
    if clean is False:
        print(f"{user} said a bad word!!")
        await message.channel.send(f"{user} said a bad word!! Shame...")
        print(message.content)
        await message.delete()
        print("Deleted...")


def get_verse():
    link = "https://beta.ourmanna.com/api/v1/get/?format=text"
    verse = requests.get(link)
    if verse.status_code == 200:
        print("VOTD: " + verse.text.rstrip("\n"))
    # rand_hour = str(random.randint(8, 19))
    # rand_minute = str(random.randint(10, 59))
    # print(rand_hour + ":" + rand_minute)
    # schedule.every().day.at(f'{rand_hour}:{rand_minute}').do(await client.get_channel(int(CHANNEL)).send(verse.text.rstrip("\n")))


client.run(TOKEN)
