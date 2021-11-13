import discord
from discord.ext import commands


class User(commands.Cog):
    def __init__(self, morax):
        self.morax = morax

    @commands.guild_only()
    @commands.command(aliases=["cn"])
    async def changeNickname(self, ctx, *, name: str = None):
        """ Change nickname. """
        await ctx.author.edit(nick=name)
        if name:
            await ctx.send(f"Successfully changed nickname to **{name}**")
        else:
            await ctx.send("Successfully removed nickname")


def setup(morax):
    morax.add_cog(User(morax))
