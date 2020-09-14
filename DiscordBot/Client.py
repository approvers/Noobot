import discord
import os
from discord.ext import tasks

from DiscordBot.MessageReceiver import MessageReceiver, PingPong
from Console.View.PingPong.PingPongConsolePresenter import PingPongConsolePresenter
from Domain.Application.PingPong.PingPongInteractor import PingPongInteractor



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def __init__(self):
        super().__init__()
        self._receiver = MessageReceiver(
            PingPong(PingPongInteractor(PingPongConsolePresenter()))
        )

    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        pass

    async def on_message(self, message: discord.Message):
        self._receiver.receive(message)