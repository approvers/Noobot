import discord
import os
from discord.ext import tasks

from DiscordBot.MessageView.MessageSender import MessageSender
from DiscordBot.MessageReceiver import MessageReceiver
from DiscordBot.Adapter.PingPong.PingPong import PingPong
from DiscordBot.Adapter.PingPong.PingPongPresenter import PingPongPresenter 
from Domain.Application.PingPong.PingPongInteractor import PingPongInteractor



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def __init__(self):
        super().__init__()
        sender = MessageSender()
        self._receiver = MessageReceiver(
            sender,
            PingPong(PingPongInteractor(PingPongPresenter(sender)))
        )

    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        pass

    async def on_message(self, message: discord.Message):
        await self._receiver.receive(message)