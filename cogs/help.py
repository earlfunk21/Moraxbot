from typing import Optional, Set

import discord
from discord.ext import commands


class HelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

    async def _help_embed(self, title: str,
                          description: Optional[str] = None,
                          mapping: Optional[dict] = None,
                          command_set: Optional[Set[commands.Command]] = None
                          ):
        embed = discord.Embed(title=title, color=0x00ff00)
        if description:
            embed.description = description
        if command_set:
            filtered = await self.filter_commands(command_set, sort=True)
            for command in filtered:
                embed.add_field(name=self.get_command_signature(command), value=command.help, inline=False)
        if mapping:
            for cog, command_set in mapping.items():
                filtered = await self.filter_commands(command_set, sort=True)
                if not filtered:
                    continue
                name = cog.qualified_name if cog else "No Category"
                cmd_list = "\u2002".join(
                    f"`|{cmd.name}`" for cmd in filtered
                )
                value = (
                    f"Prefix\"-\" ex. -help\n{cog.description}\n{cmd_list}"
                    if cog and cog.description
                    else cmd_list
                )
                embed.add_field(name=name, value=value, inline=False)
        return embed

    async def send_bot_help(self, mapping: dict):
        embed = await self._help_embed(
            title="Morax Commands",
            description=self.context.bot.description,
            mapping=mapping,
        )
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed = await self._help_embed(
            title=command.qualified_name,
            description=command.help,
            command_set=command.commands if isinstance(command, commands.Group) else None
        )
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        pass


class HelpCog(commands.Cog, name="Help"):
    """ Shows help info about commands """

    def __init__(self, morax):
        self._original_help_command = morax.help_command
        morax.help_command = HelpCommand()
        morax.help_command.cog = self
        self.morax = morax

    def cog_unload(self):
        self.morax.help_command = self._original_help_command


def setup(morax: commands.bot):
    morax.add_cog(HelpCog(morax))
