import importlib

import discord
import sys
import time
from discord import Embed
from discord.channel import DMChannel
from discord.ext import commands

from utils import trace_back, config


class Admin(commands.Cog):
    def __init__(self, morax) -> None:
        self.morax = morax
        self.owner = morax.get_user(config()["owner"])

    async def in_channel(self, ctx):
        return ctx.author.


    @commands.dm_only()
    @commands.is_owner()
    @commands.command()
    async def load(self, ctx, directory: str) -> None:
        """ Load a Cog extension"""
        try:
            self.morax.load_extension(f"cogs.{directory}")
            await ctx.send(embed=Embed(title=f"Cog Loaded {directory}"))
        except Exception as e:
            await ctx.send(trace_back(e))

    @commands.dm_only()
    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, directory: str) -> None:
        """ Unload a Cog extension"""
        try:
            self.morax.unload_extension(f"cogs.{directory}")
            await ctx.send(embed=Embed(title=f"Cog unloaded {directory}"))
        except Exception as e:
            await ctx.send(trace_back(e))

    @commands.dm_only()
    @commands.is_owner()
    @commands.command()
    async def reload(self, ctx, directory: str) -> None:
        """ Reload a Cog extension"""
        try:
            self.morax.reload_extension(f"cogs.{directory}")
            await ctx.send(embed=Embed(title=f"Cog reloaded {directory}"))
        except Exception as e:
            await ctx.send(trace_back(e))

    @commands.dm_only()
    @commands.is_owner()
    @commands.command()
    async def reloadUtils(self, ctx, name: str) -> None:
        """ Reload a Utils module """
        try:
            module_name = importlib.import_module(f"utils.{name}")
            importlib.reload(module_name)
            await ctx.send(f"Module Reloaded {name}")
        except Exception as e:
            await ctx.send(trace_back(e))

    @commands.dm_only()
    @commands.is_owner()
    @commands.command(help=" - logging off", aliases=["close", "poweroff", "turnoff, logoff"])
    async def logout(self, ctx):
        """ Morax-bot is logging off """
        await ctx.send("Bye")
        time.sleep(1)
        sys.exit(0)

    @commands.dm_only()
    @commands.is_owner()
    @commands.command(help=" - Send a messasge to the User", aliases=["send", "dm"])
    async def pm(self, ctx, user: discord.User, *, message: str):
        """ Sending a message to Specific User"""
        try:
            await user.send(message)
            await ctx.send(f"Message send to {user}")
        except Exception as e:
            await ctx.send(trace_back(e))

    @commands.command()
    async def kick(self, ctx, user: discord.User, *, reason: str = None):
        """ Kicking a member"""
        try:
            await ctx.guild.kick(user, reason=reason)
            await ctx.send(f"{user.name}\nhas been Kicked\nBecause of {reason}")
            return await ctx.send(f"```diff\n -Could find user named {user}")
        except Exception as e:
            await DMChannel.send(self.owner, trace_back(e))

    @commands.is_owner()
    @commands.command()
    async def ban(self, ctx, user: discord.User, *, reason: str = None):
        """ Banning a member"""
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"{user.name}\nhas been Banned\nBecause of {reason}")

    @commands.is_owner()
    @commands.command()
    async def unban(self, ctx, user: discord.User, *, reason: str = "Nothing"):
        """ Unbanning a banned member """
        await ctx.guild.unban(user, reason=reason)
        await ctx.send(f"{user.name}\nSuccessfully Unbanned")

    @commands.is_owner()
    @commands.command()
    async def banList(self, ctx):
        """ Show Ban list"""
        await ctx.send(await ctx.guild.bans())


def setup(morax):
    morax.add_cog(Admin(morax))
