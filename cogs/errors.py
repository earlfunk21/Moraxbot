import discord
import traceback

from discord.ext import commands


def trace_back(err, advance: bool = True):
    """ debug your code anywhere """
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = '```py\n{1}{0}: {2}\n```'.format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"


class Errors(commands.Cog):
    def __init__(self, morax):
        self.morax = morax

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        elif isinstance(error, commands.MissingPermissions):
            message = "You are missing the required permissions to run this command!"
        elif isinstance(error, commands.UserInputError):
            message = "Something about your input was wrong, please check your input and try again!"
        else:
            message = "Oh no! Something went wrong while running the command!"
        channel = discord.utils.get(ctx.guild.channels, name="bot-errors")
        await channel.send(trace_back(error))
        await ctx.send("```py\n{0}\n```".format(message))


def setup(morax):
    morax.add_cog(Errors(morax))
