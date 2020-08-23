import discord
from typing import Union

from DiscordBot.ConsoleApp.ConsoleMessage import ConsoleMessage
from DiscordBot.User.Command.IUserCommand import IUserCommand
from UseCase.User.KP.Add.IAddKPUseCase import IAddKPUseCase
from UseCase.User.KP.Add.AddKPInputData import AddKPInputData



class AddKPCommand(IUserCommand):
    def __init__(self, addKPUseCase: IAddKPUseCase):
        self._addKPUseCase = addKPUseCase

    def execute(self, message: Union[discord.Message, ConsoleMessage]):
        user_id: int = None

        if isinstance(message, discord.Message):
            user_id = message.author.id
        else:
            user_id = message.user_id

        input_data = AddKPInputData(user_id)

        self._addKPUseCase.handle(input_data)