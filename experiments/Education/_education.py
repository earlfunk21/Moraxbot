import discord
from discord.ext import commands
from ._infotech import ComputerSystem as CS
from ._math import Statistics
import asyncio
from utils import config



class Education(commands.Cog):
    def __init__(self, Morax) -> None:
        super().__init__()
        self.Morax = Morax
        
    @commands.command()
    async def setupEducation(self, ctx):
        await ctx.send(embed=discord.Embed(title="Setting Up.. The Education"), delete_after=3)
        role = await ctx.guild.create_role(name="Student", colour=discord.Colour.random(), hoist=True)
        category = await ctx.guild.create_category(name="Education")
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
            role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True)
        }
        await category.edit(overwrites=overwrites)
        await ctx.guild.create_text_channel("bot-apprentice", category=category, sync_permissions=True)
        await ctx.guild.create_voice_channel("students-meeting", category=category, sync_permissions=True)
        await asyncio.sleep(3)
        await ctx.send(embed=discord.Embed(title="Education Created."), delete_after=5)


    @commands.command()
    async def unpacked(self, ctx, n):
        UDF = "".join(CS().Unpacked(n))
        HD = "".join(CS().hexadecimal(CS().Unpacked(n)))
        await ctx.send(UDF)
        await ctx.send("Hexadecimal: " + HD)

    @commands.command()
    async def packed(self, ctx, n):
        PDF = "".join(CS().packed(n))
        HD = "".join(CS().hexadecimal(CS().packed(n)))
        await ctx.send(PDF)
        await ctx.send("Hexadecimal: " + HD)

    @commands.command(aliases=["tv_hexa"])
    async def truevalue_hexa(self, ctx, n):
        truevalue = CS().truevalue(Hexadecimal=n)
        await ctx.send(truevalue)

    @commands.command(aliases=["tv_octa"])
    async def truevalue_octa(self, ctx, n):
        truevalue = CS().truevalue(Octa=n)
        await ctx.send(truevalue)

    @commands.command(aliases=["tv_decimal"])
    async def truevalue_deci(self, ctx, n):
        truevalue = CS().truevalue(Decimal=n)
        await ctx.send(truevalue)

    @commands.command(aliases=["tv_binary"])
    async def truevalue_bina(self, ctx, n):
        truevalue = CS().truevalue(Binary=n)
        await ctx.send(truevalue)


##################################################
###### MATH #####################################

    @commands.command(help=" - Statistic")
    async def mean(self, ctx, *, n):
        mean = Statistics(n).mean()
        await ctx.send(mean)
    
    @commands.command(help=" - Statistic")
    async def median(self, ctx, *, n):
        median = Statistics(n).median()
        await ctx.send(median)
    
    @commands.command(help=" - Statistic")
    async def mode(self, ctx, *, n):
        mode = Statistics(n).mode()
        await ctx.send(mode)

    @commands.command()
    async def arith(self, ctx, n: int, x, *a: int):
        d = a[1] - a[0]
        x = a[0] + (n - 1) * d
        await ctx.send(f"The {n}ᵗʰterm of the given sequence is {x}")


def setup(Morax):
    Morax.add_cog(Education(Morax))