
import discord
from discord.ext import commands

from utils.permissions import is_owner


class Test(commands.Cog):
    def __init__(self, morax):
        self.morax = morax

    @commands.check(is_owner)
    @commands.command(pass_context=True)
    async def test(self, ctx, member: discord.Member):
        channel = ctx.message.author.voice.channel
        if channel and member.voice:
            await member.move_to(channel)
        else:
            return await ctx.reply("```You or the member you mention are not connected to a voice channel```")


def setup(morax):
    morax.add_cog(Test(morax))
