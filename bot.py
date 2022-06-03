import discord, os
from discord.ext import commands

bot = commands.Bot(command_prefix="-", help_command=None, intents=discord.Intents.all())

# Return token from a seperate .txt file
def get_token():
    with open("./token.txt", 'r') as file:
        return file.readlines()[0].strip()

# Load cogs from a folder named 'cogs'
for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")
    else:
        print(f"Unable to load {filename[:-3]}")

bot.run(get_token())
