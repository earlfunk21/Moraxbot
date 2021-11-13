import discord

from discord.ext import commands

from utils.create import Create


class Events(commands.Cog):
    def __init__(self, morax):
        self.morax = morax

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        create = Create(guild)
        await create.role("Moderator")
        moraxCategory = await create.category("Morax-Commands")
        await create.textChannel("morax-cmd", overwrites=None, category=moraxCategory)
        await create.textChannel("bot-errors",
                                 overwrites={guild.default_role: discord.PermissionOverwrite(send_messages=False)},
                                 category=moraxCategory
                                 )

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(title=f"Hi! {member.name}")
            embed.add_field(name="Welcome to the Morax server",
                            value='use "-help" if you want help')
            embed.set_image(url=member.avatar_url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Morax bot is Ready!!!")


def setup(morax):
    morax.add_cog(Events(morax))
