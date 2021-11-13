import discord

from discord.ext import commands

from utils.permissions import in_cmd_channel


class Text(commands.Cog):
    def __init__(self, morax):
        self.morax = morax

    @commands.check(in_cmd_channel)
    @commands.command()
    async def link(self, ctx, link: str, *, name: str = "Click here"):
        """ link to clickable text """
        await ctx.message.delete()
        embed = discord.Embed()
        embed.description = "[{1}]({0})".format(link, name)
        await ctx.send(embed=embed)

    @commands.check(in_cmd_channel)
    @commands.command()
    async def python(self, ctx, *, code: str):
        """ python code """
        await ctx.message.delete()
        embed = discord.Embed(title="Python code")
        message = '''```py\n{}\n```'''.format(code)
        embed.description = message
        await ctx.send(embed=embed)

    @commands.check(in_cmd_channel)
    @commands.command()
    async def cpp(self, ctx, *, code: str):
        """ C/CPP code """
        await ctx.message.delete()
        embed = discord.Embed(title="C/CPP code")
        message = '''```cpp\n{}\n```'''.format(code)
        embed.description = message
        await ctx.send(embed=embed)


def setup(morax):
    morax.add_cog(Text(morax))
