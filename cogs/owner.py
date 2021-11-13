import importlib

import discord
import sys
import time
from discord import Embed
from discord.ext import commands

from utils.permissions import is_owner, in_cmd_channel


class Owner(commands.Cog):
    def __init__(self, morax) -> None:
        self.morax = morax

    @commands.check(is_owner)
    @commands.check(in_cmd_channel)
    @commands.command()
    async def load(self, ctx, directory: str) -> None:
        """ Load a Cog extension"""
        self.morax.load_extension(f"cogs.{directory}")
        await ctx.send(embed=Embed(title=f"Cog Loaded {directory}"))

    @commands.check(is_owner)
    @commands.check(in_cmd_channel)
    @commands.command()
    async def unload(self, ctx, directory: str) -> None:
        """ Unload a Cog extension"""
        self.morax.unload_extension(f"cogs.{directory}")
        await ctx.send(embed=Embed(title=f"Cog unloaded {directory}"))

    @commands.check(is_owner)
    @commands.check(in_cmd_channel)
    @commands.command()
    async def reload(self, ctx, directory: str) -> None:
        """ Reload a Cog extension"""
        self.morax.reload_extension(f"cogs.{directory}")
        await ctx.send(embed=Embed(title=f"Cog reloaded {directory}"))

    @commands.check(is_owner)
    @commands.check(in_cmd_channel)
    @commands.command()
    async def reloadUtils(self, ctx, name: str) -> None:
        """ Reload a Utils module """
        module_name = importlib.import_module(f"utils.{name}")
        importlib.reload(module_name)
        await ctx.send(f"Module Reloaded {name}")

    @commands.check(is_owner)
    @commands.check(in_cmd_channel)
    @commands.command(help=" - logging off", aliases=["close", "poweroff", "turnoff, logoff"])
    async def logout(self, ctx):
        """ Morax-bot is logging off """
        await ctx.send("Bye")
        time.sleep(1)
        sys.exit(0)


def setup(morax):
    morax.add_cog(Owner(morax))
