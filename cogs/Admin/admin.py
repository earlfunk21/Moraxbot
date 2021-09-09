import discord
import importlib
from discord.ext import commands
from typing import TypeVar
from utils import trace_back


class Admin(commands.Cog):
    def __init__(self, Morax) -> None:
        self.Morax = Morax


    """ Load a Cog extension"""
    @commands.dm_only()
    @commands.is_owner()
    @commands.command()
    async def load(self, ctx, dir: str) -> None:
        try:
            self.Morax.load_extension(f"cogs.{dir}")
            await ctx.send(f"Cog Loaded {dir}")
        except Exception as e:
            return await ctx.send(trace_back(e))


    """ Unload a Cog extension"""
    @commands.dm_only()
    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, dir: str) -> None:
        try:
            self.Morax.unload_extension(f"cogs.{dir}")
            await ctx.send(f"Cog Unloaded {dir}")
        except Exception as e:
            return await ctx.send(trace_back(e))


    """ Reload a Cog extension"""
    @commands.dm_only()
    @commands.is_owner()
    @commands.command()
    async def reload(self, ctx, dir: str) -> None:
        try:
            await self.unload(ctx, dir)
            await self.load(ctx, dir)
            await ctx.send(f"Cog Reloaded {dir}")
        except Exception as e:
            return await ctx.send(trace_back(e))


    """ Reload a Utils module """
    @commands.dm_only()
    @commands.is_owner()
    @commands.command()
    async def reloadutils(self, ctx, name: str) -> None:
        name = f"utils/{name}.py"
        try:
            module_name = importlib.import_module(f"utils.{name}")
            importlib.reload(module_name)
            await ctx.send(f"Module Reloaded {name}")
        except ModuleNotFoundError:
            return await ctx.send(f"Couldn't find module {name}")
        except Exception as e:
            error = trace_back(e)
            return await ctx.send(f"Module {name} returned error and was not reloaded...\n{error}")
        