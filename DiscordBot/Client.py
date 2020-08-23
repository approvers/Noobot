import discord
import os
from discord.ext import tasks

from DiscordBot.MessageReceiver import MessageReceiver



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def __init__(self, receiver: MessageReceiver):
        super().__init__()
        self._receiver = receiver

    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        pass

    async def on_message(self, message: discord.Message):
        await self._receiver.receive(message)