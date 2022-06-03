import discord
from discord.ext import commands

class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("----------Connected to Bot----------\n"
             f"Bot Username: {self.bot.user.name}\n"
             f"Bot ID: {self.bot.user.id}")

        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="-help"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(f"We hope you enjoy your stay at {member.guild}, be sure to verify and read the rules!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"There was a missing required argument.")

        elif isinstance(error, commands.MissingPermissions or commands.MissingAnyRole):
            await ctx.send("You are missing a required role or permission.")

        elif isinstance(error, commands.CommandNotFound):
            pass

        elif isinstance(error, commands.BadArgument):
            await ctx.send("There was a bad argument, please retype the command.")

        else:
            print(f"----------\n{ctx.message.author} in {ctx.message.channel}:\nTried invoking '{ctx.message.content}' with error '{error}'\n----------")

def setup(bot):
    bot.add_cog(CommandEvents(bot))
    