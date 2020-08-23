import discord
import os
from discord.ext import tasks

from DiscordBot.MessageReceiver import MessageReceiver
from DiscordBot.Startup import Startup
from DiscordBot.ConsoleApp.ConsoleMessage import ConsoleMessage



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



if __name__ == "__main__":
    if __debug__:
        receiver: MessageReceiver = Startup.console_receiver()
        user_id: int = 0

        while True:
            content:str  = input()
            message = ConsoleMessage(content, user_id)
            receiver.input(message)

    receiver: MessageReceiver = Startup.message_receiver()
    client = Client(receiver)
    client.run()
