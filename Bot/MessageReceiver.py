import discord

from Bot.User.UserController import UserController
from Domain.Application.AddKPInteractor import AddKPInteractor
from Domain.Domain.UserList import UserList



class MessageReceiver:
    def __init__(self):
        self._user_controller = UserController(
            AddKPInteractor(UserList())
        )

    async def receive(self, message: discord.Message):
        await self._user_controller.on_message(message)