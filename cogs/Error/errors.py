import discord
from discord.errors import Forbidden, HTTPException
from discord.ext import commands
from utils import trace_back, config
from discord.channel import DMChannel
import time

class Errors(commands.Cog):
    def __init__(self, Morax: commands.Bot):
        self.Morax = Morax

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandOnCooldown):
            title = f"Slow it down bro!"
            description = f"Hey {ctx.author.name},Try again in {error.retry_after:.1f}s."
            em = discord.Embed(title=title, description=description)
            await ctx.send(embed=em, delete_after=30, mention_author=ctx.author.id)
            return

        elif isinstance(error, commands.CommandNotFound):
            title = 'Command not Found'

        elif isinstance(error, commands.MissingPermissions):
            title = "You are missing the required permissions"

        elif isinstance(error, commands.UserInputError):
            title = "Something about your input was wrong"

        elif isinstance(error, Forbidden):
            title="You do not have proper permissions to get the information."

        elif isinstance(error, HTTPException):
            title=" An error occurred while fetching the information."

        elif isinstance(error, ModuleNotFoundError):
            title="Module not be found"

        else:
            title = "Something went wrong while running the command!"

        owner = self.Morax.get_user(config()["owner"])
        await DMChannel.send(owner, f"{trace_back(error)}{time.strftime('%B %d/%H:%M')}")
        description=error
        em = discord.Embed(title=title, description=description)
        await ctx.send(embed=em, delete_after=30, mention_author=ctx.author.id)

