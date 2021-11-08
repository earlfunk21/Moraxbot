import importlib

import discord
import sys
import time
from discord import Embed
from discord.ext import commands

from utils import trace_back, is_owner


async def in_admin_channel(ctx):
    if ctx.channel == discord.utils.get(ctx.guild.channels, name="admin"):
        return True
    else:
        pass


async def in_server_management_channel(ctx):
    if ctx.channel == discord.utils.get(ctx.guild.channels, name="server_management"):
        return True
    else:
        pass


class Admin(commands.Cog):
    def __init__(self, morax) -> None:
        self.morax = morax

    @commands.check(is_owner)
    @commands.check(in_server_management_channel)
    @commands.command()
    async def load(self, ctx, directory: str) -> None:
        """ Load a Cog extension"""
        try:
            self.morax.load_extension(f"cogs.{directory}")
            await ctx.send(embed=Embed(title=f"Cog Loaded {directory}"))
        except Exception as err:
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.check(is_owner)
    @commands.check(in_server_management_channel)
    @commands.command()
    async def unload(self, ctx, directory: str) -> None:
        """ Unload a Cog extension"""
        try:
            self.morax.unload_extension(f"cogs.{directory}")
            await ctx.send(embed=Embed(title=f"Cog unloaded {directory}"))
        except Exception as err:
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.check(is_owner)
    @commands.check(in_server_management_channel)
    @commands.command()
    async def reload(self, ctx, directory: str) -> None:
        """ Reload a Cog extension"""
        try:
            self.morax.reload_extension(f"cogs.{directory}")
            await ctx.send(embed=Embed(title=f"Cog reloaded {directory}"))
        except Exception as err:
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.check(is_owner)
    @commands.check(in_server_management_channel)
    @commands.command()
    async def reloadUtils(self, ctx, name: str) -> None:
        """ Reload a Utils module """
        try:
            module_name = importlib.import_module(f"utils.{name}")
            importlib.reload(module_name)
            await ctx.send(f"Module Reloaded {name}")
        except Exception as err:
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.check(is_owner)
    @commands.check(in_server_management_channel)
    @commands.command(help=" - logging off", aliases=["close", "poweroff", "turnoff, logoff"])
    async def logout(self, ctx):
        """ Morax-bot is logging off """
        await ctx.send("Bye")
        time.sleep(1)
        sys.exit(0)

    @commands.check(in_server_management_channel)
    @commands.command(help=" - Send a messasge to the User", aliases=["send", "dm"])
    async def pm(self, ctx, user: discord.User, *, message: str):
        """ Sending a message to Specific User"""
        try:
            await user.send(message)
            await ctx.send(f"Message send to {user}")
        except Exception as err:
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.guild_only()
    @commands.check(in_server_management_channel)
    @commands.command()
    async def kick(self, ctx, user: discord.User, *, reason: str = None):
        """ Kicking a member"""
        try:
            await ctx.guild.kick(user, reason=reason)
            await ctx.send(f"{user.name}\nhas been Kicked\nBecause of {reason}")
            return await ctx.send(f"```diff\n -Could find user named {user}")
        except Exception as err:
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.guild_only()
    @commands.check(in_server_management_channel)
    @commands.check(is_owner)
    @commands.command()
    async def ban(self, ctx, user: discord.User, *, reason: str = "Nothing"):
        """ Banning a member"""
        try:
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(f"{user.name}\nhas been Banned\nBecause of {reason}")
        except Exception as err:
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.guild_only()
    @commands.check(in_server_management_channel)
    @commands.check(is_owner)
    @commands.command()
    async def unban(self, ctx, user: discord.User, *, reason: str = "Nothing"):
        """ Unbanning a banned member """
        try:
            await ctx.guild.unban(user, reason=reason)
            await ctx.send(f"{user.name}\nSuccessfully Unbanned")
        except Exception as err:
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.guild_only()
    @commands.command()
    async def banList(self, ctx):
        """ Show Ban list"""
        try:
            ban_list = await ctx.guild.bans()
            dict_bans = [ban._asdict() for ban in ban_list]
            user = dict_bans[0].get('user')
            await ctx.send(user)
        except Exception as err:
            if isinstance(err, IndexError):
                await ctx.send("None")
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.guild_only()
    @commands.command(aliases=["cn"])
    async def changeNickname(self, ctx, *, name: str = None):
        """ Change nickname. """
        try:
            await ctx.author.edit(nick=name)
            if name:
                await ctx.send(f"Successfully changed nickname to **{name}**")
            else:
                await ctx.send("Successfully removed nickname")
        except Exception as err:
            channel = discord.utils.get(ctx.guild.channels, name="errors")
            await channel.send(trace_back(err))

    @commands.check(is_owner)
    @commands.guild_only()
    @commands.command()
    async def setUp(self, ctx, name):
        """ setting up the commands"""
        category = discord.utils.get(ctx.guild.channels, name="Commands")
        role = discord.utils.get(ctx.guild.roles, name="Moderator")
        if role not in ctx.guild.roles:
            await ctx.guild.create_role(name="Moderator", colour=discord.Colour.random(), hoist=True)
        if category not in ctx.guild.channels:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
                role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True)
            }
            category = await ctx.guild.create_category("Commands", overwrites=overwrites, reason=None)
        try:
            if name == "admin":
                await ctx.send("Setting up management!")
                if discord.utils.get(ctx.guild.text_channels, name="server_management") not in ctx.guild.channels:
                    await ctx.guild.create_text_channel("server_management", overwrites=None, category=category, reason=None)
                if discord.utils.get(ctx.guild.text_channels, name="admin") not in ctx.guild.channels:
                    await ctx.guild.create_text_channel("admin", overwrites=None, category=category, reason=None)
                if discord.utils.get(ctx.guild.text_channels, name="errors") not in ctx.guild.channels:
                    await ctx.guild.create_text_channel("errors", overwrites=None, category=category, reason=None)
                await ctx.send("Setup finished!")
        except Exception as err:
            await ctx.send(trace_back(err))


def setup(morax):
    morax.add_cog(Admin(morax))
