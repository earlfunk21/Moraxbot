import os
import discord
from discord.ext.commands import Bot

Morax = Bot(
    command_prefix="-",
    intents=discord.Intents.all(),
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False),
    command_attrs=dict(hidden=True),
    help_command=None,
)

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        Morax.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    try:
        Morax.run("ODU3NDk0Mzg4MTg0MDU1ODE4.YNQZ4Q.EzkHc08SheHuuTaOpt3QavB9R4o")
    except Exception as e:
        print(f"Error when logging in {e}")
