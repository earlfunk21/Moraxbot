
import discord

from discord.ext import commands

from utils.create import Create


class Events(commands.Cog):
    def __init__(self, morax):
        self.morax = morax

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        create = Create(guild)
        moraxCategory = await create.category("Morax-Commands")
        await create.textChannel("morax-cmd", category=moraxCategory)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(send_messages=False)
        }
        await create.textChannel("bot-errors",
                                 overwrites=overwrites,
                                 category=moraxCategory
                                 )

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(title=f"Hi! {member.name}")
            embed.add_field(name="Welcome to the Kulto De Morax",
                            value='use "-help" if you want help')
            embed.set_image(url=member.avatar_url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is not None:
            if before.channel.category == discord.utils.get(before.channel.guild.categories,
                                                            name="Private Rooms 🔇"):
                if len(before.channel.members) == 0:
                    await before.channel.delete()

        if after.channel is not None:
            if after.channel.name == "BebeTime":
                create = Create(after.channel.guild)
                await create.bebeTime(member, after)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.morax:
            return
        if message.content.startswith("#include"):
            await message.delete()
            embed = discord.Embed(title="C or C++")
            codes = '''```cpp\n{}\n```'''.format(message.content)
            embed.description = codes
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Morax bot is Ready!!!")


def setup(morax):
    morax.add_cog(Events(morax))
