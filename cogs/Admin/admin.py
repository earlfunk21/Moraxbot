import discord, sys, time
import importlib
from discord.ext import commands
from utils import trace_back


class Admin(commands.Cog):
    def __init__(self, Morax) -> None:
        self.Morax = Morax


    """ Load a Cog extension"""
    @commands.dm_only()
    @commands.is_owner()
    @commands.command(help=" - Load a Cog extension")
    async def load(self, ctx, dir: str) -> None:
        self.Morax.load_extension(f"cogs.{dir}")
        await ctx.send(f"Cog Loaded {dir}")


    """ Unload a Cog extension"""
    @commands.dm_only()
    @commands.is_owner()
    @commands.command(help=" - Unload a Cog extension")
    async def unload(self, ctx, dir: str) -> None:
        self.Morax.unload_extension(f"cogs.{dir}")
        await ctx.send(f"Cog Unloaded {dir}")


    """ Reload a Cog extension"""
    @commands.dm_only()
    @commands.is_owner()
    @commands.command(help=" - Reload a Cog extension")
    async def reload(self, ctx, dir: str) -> None:
        self.Morax.unload_extension(f"cogs.{dir}")
        self.Morax.load_extension(f"cogs.{dir}")
        await ctx.send(f"Cog Reloaded {dir}")


    """ Reload a Utils module """
    @commands.dm_only()
    @commands.is_owner()
    @commands.command(help=" - Reload a Utils module")
    async def reloadutils(self, ctx, name: str) -> None:
        module_name = importlib.import_module(f"utils.{name}")
        importlib.reload(module_name)
        await ctx.send(f"Module Reloaded {name}")
    

    """ Moraxbot is logging off """
    @commands.dm_only()
    @commands.is_owner()
    @commands.command(help=" - logging off", aliases=["close", "poweroff", "turnoff"])
    async def logout(self, ctx):
        await ctx.send("Bye")
        time.sleep(1)
        sys.exit(0)


    """ Sending a message to Specific User"""
    @commands.dm_only()
    @commands.is_owner()
    @commands.command(help=" - Send a messasge to the User", aliases=["send", "dm"])
    async def pm(self, ctx, user: discord.User, *, message: str):
        await user.send(message)
        await ctx.send(f"Message send to {user}")

    """ Kicking a member"""
    @commands.is_owner()
    @commands.command()
    async def ban(self, ctx, user: discord.User, *, reason: str=None):
        await ctx.guild.kick(user, reason=reason)
        await ctx.send(f"{user.name}\nhas been Kicked\nBecause of {reason}")


    """ Banning a member"""
    @commands.is_owner()
    @commands.command()
    async def ban(self, ctx, user: discord.User, *, reason: str=None):
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"{user.name}\nhas been Banned\nBecause of {reason}")


    """ Unbanning a banned member """
    @commands.is_owner()
    @commands.command()
    async def unban(self, ctx, user: discord.User, *, reason: str="Nothing"):
        await ctx.guild.unban(user, reason=reason)
        await ctx.send(f"{user.name}\nSuccessfully Unbanned")
        
    @commands.is_owner()
    @commands.command()
    async def banlist(self, ctx):
        await ctx.send(await ctx.guild.bans())
