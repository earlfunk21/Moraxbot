import discord

from discord.ext import commands

from utils.create import Create
from utils.permissions import in_cmd_channel


class Moderator(commands.Cog):
    def __init__(self, morax):
        self.morax = morax

    @commands.has_role("Moderator")
    @commands.check(in_cmd_channel)
    @commands.guild_only()
    @commands.command()
    async def kick(self, ctx, user: discord.User, *, reason: str = None):
        """ Kicking a member"""
        await ctx.guild.kick(user, reason=reason)
        if reason is not None:
            await ctx.reply(f"{user.name}\nhas been Kicked\nBecause of {reason}", mention_author=False)
        else:
            await ctx.reply(f"{user.name}\nhas been Kicked", mention_author=False)

    @commands.guild_only()
    @commands.has_role("Moderator")
    @commands.check(in_cmd_channel)
    @commands.command()
    async def ban(self, ctx, user: discord.User, *, reason: str = None):
        """ Banning a member"""
        await ctx.guild.ban(user, reason=reason)
        if reason is not None:
            await ctx.reply(f"{user.name}\nhas been Banned\nBecause of {reason}\n", mention_author=False)
        else:
            await ctx.reply(f"{user.name}\nhas been Banned", mention_author=False)

    @commands.guild_only()
    @commands.has_role("Moderator")
    @commands.check(in_cmd_channel)
    @commands.command()
    async def unban(self, ctx, user: discord.User, *, reason: str = "Nothing"):
        """ Unbanning a banned member """
        await ctx.guild.unban(user, reason=reason)
        await ctx.reply(f"{user.name}\nSuccessfully Unbanned", mention_author=False)

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.has_role("Moderator")
    @commands.check(in_cmd_channel)
    @commands.command(help=" - Send a messasge to the User", aliases=["send", "dm"])
    async def pm(self, ctx, user: discord.User, *, message: str):
        """ Sending a message to Specific User"""
        await user.send(message)
        await ctx.reply(f"Message send to {user}", mention_author=False)

    @commands.check(in_cmd_channel)
    @commands.has_role("Moderator")
    @commands.guild_only()
    @commands.command()
    async def createRole(self, ctx, role: str):
        """ create a role """
        create = Create(ctx.guild)
        if await create.role(role) is None:
            return await ctx.send("```py\nAlready in this guild\n```")
        await ctx.reply("```css\n.{0} has been created!\n```".format(role), mention_author=False)

    @commands.check(in_cmd_channel)
    @commands.has_role("Moderator")
    @commands.command()
    async def addRole(self, ctx, role: discord.Role, member: discord.Member):
        """ adding a role of a members """
        if role in ctx.guild.roles:
            await member.add_roles(role)
            await ctx.reply("```py\n{0} added to role {1}\n```".format(member, role), mention_author=False)


def setup(morax):
    morax.add_cog(Moderator(morax))
