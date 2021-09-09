import discord
from discord.ext.commands import DefaultHelpCommand

class HelpCommand(DefaultHelpCommand):
    def get_destination(self):
        return super().get_destination()
    
    async def send_error_message(self, error):
        return await super().send_error_message(error)
    
    async def send_pages(self):
        return await super().send_pages()

    async def send_command_help(self, command):
        return await super().send_command_help(command)