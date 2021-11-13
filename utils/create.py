import discord


class Create(object):
    def __init__(self, guild: discord.Guild):
        self.guild = guild

    async def role(self,
                   name: str,
                   hoist: bool = True
                   ):
        role = discord.utils.get(self.guild.roles, name=name)
        if role is None:
            return await self.guild.create_role(name=name, colour=discord.Colour.random(), hoist=hoist)
        return role

    async def textChannel(self,
                          name: str,
                          category: discord.CategoryChannel = None,
                          overwrites: dict = None
                          ):
        channel = discord.utils.get(self.guild.text_channels, name=name)
        if channel is None:
            return await self.guild.create_text_channel(name, overwrites=overwrites, category=category, reason=None)
        return channel

    async def category(self,
                       name: str,
                       overwrites: dict = None,
                       reason: str = None
                       ):
        category = discord.utils.get(self.guild.categories, name=name)
        if category is None:
            return await self.guild.create_category(name, overwrites=overwrites, reason=reason)
        return category
