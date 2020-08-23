import discord

from DiscordBot.ConsoleApp.ConsoleMessage import ConsoleMessage
from DiscordBot.User.UserController import UserController
from DiscordBot.MessageSender import MessageSender
from Domain.Domain.User.IUserRepository import IUserRepository
from Domain.Application.User.KP.AddKPInteractor import AddKPInteractor
from Domain.Application.User.KP.GetKPInteractor import GetKPInteractor
from DiscordBot.User.Command.KP.Get.GetKPConsolePresenter import GetKPConsolePresenter
from DiscordBot.User.Command.KP.Get.GetKPMessagePresenter import GetKPMessagePresenter



class MessageReceiver:
    def __init__(
        self,
        sender: MessageSender,
        user_controller: UserController
    ):
        self._user_controller = user_controller
        self._sender = sender

    async def receive(self, message: discord.Message):
        self._user_controller.on_message(message)
        await self._sender.send(message.channel)

    def input(self, message: ConsoleMessage):
        self._user_controller.on_message(message)