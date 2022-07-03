import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="-", help_command=None, intents=discord.Intents.all())

# Get bot token from a file called 'token.txt'
def get_token():
    with open("./token.txt", 'r') as file:
        return file.readlines()[0].strip()

# Load all .py files from a folder named 'cogs'
def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            bot.load_extension(f"cogs.{filename[:-3]}")
        else:
            print(f"Unable to load {filename[:-3]}")


def main():
    load_cogs()
    bot.run(get_token())

# Run if the file is being ran directly
if __name__ == "__main__":
    main()
