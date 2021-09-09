import os
import discord
from discord.ext.commands import Bot
from utils import config, HelpCommand

owner = config()["owner"]
Morax = Bot(
    command_prefix="-",
    owner_id=owner,
    intents=discord.Intents.all(),
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False),
    help_command=HelpCommand(),
    command_attrs=dict(hidden=True)
    )

@Morax.event
async def on_ready():
    print("Moraxbot is Ready!!!")


for file in os.listdir("cogs"):
    Morax.load_extension(f"cogs.{file}")

if __name__=="__main__":
    try:
        Morax.run(config()["token"])
    except Exception as e:
        print(f"Error when logging in {e}")