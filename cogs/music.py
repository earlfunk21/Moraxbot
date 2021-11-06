from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, morax):
        self.morax = morax


def setup(morax):
    morax.add_cog(Music(morax))
