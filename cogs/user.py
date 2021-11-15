
import discord
from discord.ext import commands

from utils.permissions import in_cmd_channel, in_voice_channel


class User(commands.Cog):
    def __init__(self, morax):
        self.morax = morax

    @commands.check(in_cmd_channel)
    @commands.guild_only()
    @commands.command(aliases=["cn"])
    async def nick(self, ctx, *, name: str = None):
        """ Change nickname. """
        await ctx.author.edit(nick=name)
        if name:
            await ctx.reply(f"Successfully changed nickname to **{name}**")
        else:
            await ctx.reply("Successfully removed nickname")

    @commands.check(in_voice_channel)
    @commands.guild_only()
    @commands.check(in_cmd_channel)
    @commands.command()
    async def move(self, ctx, member: discord.Member):
        """ Moving members to your voice channel """
        channel = ctx.message.author.voice.channel
        if member.voice:
            await member.move_to(channel)
        else:
            return await ctx.reply("```You or the member you mention are not connected to a voice channel```")


def setup(morax):
    morax.add_cog(User(morax))
