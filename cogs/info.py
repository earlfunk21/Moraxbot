import discord

from discord.ext import commands

from utils.permissions import in_cmd_channel


class Information(commands.Cog):
    def __init__(self, morax):
        self.morax = morax

    @commands.check(in_cmd_channel)
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
                await ctx.send("```py\nNone\n```")

    @commands.check(in_cmd_channel)
    @commands.command()
    async def ping(self, ctx):
        ms = str(round(self.morax.latency * 1000))
        await ctx.send("```css\n.{0}ms\n```".format(ms))

    @commands.check(in_cmd_channel)
    @commands.command()
    async def avatar(self, ctx, member: discord.User = None):
        user = ctx.author
        if member:
            user = member
        avatar = user.avatar_url
        avatar_as = user.avatar_url_as
        embed = discord.Embed(title="Avatar for {0}".format(ctx.author.name),
                              description="Links:\n[webp]({0})| [jpg]({1})| [png]({2})".format(
                                  avatar_as(static_format='webp'),
                                  avatar_as(static_format='jpg'),
                                  avatar_as(static_format='png'),
                                  )
                              )
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)

    @commands.check(in_cmd_channel)
    @commands.command()
    async def roles(self, ctx):
        embed = discord.Embed(title="Roles")
        for role in ctx.guild.roles:
            embed.add_field(name=role.name, value=f"ID: {role.id}", inline=False)
        await ctx.send(embed=embed)


def setup(morax):
    morax.add_cog(Information(morax))
