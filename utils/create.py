import random
import string

import discord


class Create(object):
    def __init__(self, guild: discord.Guild):
        self.guild = guild

    async def role(self,
                   name: str,
                   hoist: bool = False,
                   colour=discord.Colour.random()
                   ):
        role = discord.utils.get(self.guild.roles, name=name)
        if role is None:
            return await self.guild.create_role(name=name, colour=colour, hoist=hoist)
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

    async def voiceChannel(self,
                           name: str,
                           category: discord.CategoryChannel = None,
                           overwrites: dict = None
                           ):
        channel = discord.utils.get(self.guild.voice_channels, name=name)
        if channel is None:
            return await self.guild.create_voice_channel(name, overwrites=overwrites, category=category, reason=None)
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

    async def bebeTime(self,
                       member,
                       after
                       ):
        create = Create(after.channel.guild)
        rand = []
        for _ in range(5):
            rand.append(random.choice(string.ascii_letters))
        name = "{}".format("".join(rand))
        overwrites = {
            after.channel.guild.default_role: discord.PermissionOverwrite(send_messages=False, connect=False,
                                                                          view_channel=False),
            member: discord.PermissionOverwrite(connect=True, view_channel=True)
        }
        channel = await create.voiceChannel(name,
                                            overwrites=overwrites)
        await member.move_to(channel)
