import os
import discord
from discord.ext.commands import Bot
from utils import config

Morax = Bot(
    command_prefix="-",
    intents=discord.Intents.all(),
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False),
    command_attrs=dict(hidden=True)
    )


@Morax.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        embed = discord.Embed(title=f"Hi! {member.name}")
        embed.add_field(name="Welcome to the Morax server",
                        value='use "-help" if you want help')
        embed.set_image(url=member.avatar_url)
        await channel.send(embed=embed)


@Morax.event
async def on_ready():
    print("Moraxbot is Ready!!!")


for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        Morax.load_extension(f"cogs.{filename[:-3]}")

if __name__=="__main__":
    try:
        Morax.run(config()["token"])
    except Exception as e:
        print(f"Error when logging in {e}")