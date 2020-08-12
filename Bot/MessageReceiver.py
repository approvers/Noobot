import discord

from Bot.KasuUserController import KasuUserController
from Domain.Application.KasuCoefficientInteractor import KasuCoefficientInteractor



class MessageReceiver:
    def __init__(self):
        self._user_controller = KasuUserController(
            KasuCoefficientInteractor()
        )

    async def receive(self, message: discord.Message):
        await self._user_controller.on_message(message)