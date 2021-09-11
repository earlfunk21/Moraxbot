import discord
from discord.ext import commands

class Listener(commands.Cog):
    def __init__(self, Morax) -> commands.Bot:
        super().__init__()
        self.Morax = Morax
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(title=f"Hi! {member.name}")
            embed.add_field(name="Welcome to the Morax server",
                            value='use "-help" if you want help')
            embed.set_image(url=member.avatar_url)
            await channel.send(embed=embed)
