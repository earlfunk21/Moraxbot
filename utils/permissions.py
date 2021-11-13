import discord

from utils import default

owners = default.config()["owners"]


def is_owner(ctx):
    """ Checks if the author is one of the owners """
    return ctx.author.id in owners


async def in_cmd_channel(ctx):
    if ctx.channel == discord.utils.get(ctx.guild.channels, name="morax-cmd"):
        return True
    else:
        pass
