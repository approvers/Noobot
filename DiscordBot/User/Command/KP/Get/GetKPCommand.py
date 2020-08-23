import discord
from typing import Union

from DiscordBot.ConsoleApp.ConsoleMessage import ConsoleMessage
from DiscordBot.User.Command.IUserCommand import IUserCommand
from UseCase.User.KP.Get.IGetKPUseCase import IGetKPUseCase
from UseCase.User.KP.Get.GetKPInputData import GetKPInputData



class GetKPCommand(IUserCommand):
    def __init__(self, getKPUseCase: IGetKPUseCase):
        self._getKPUseCase = getKPUseCase

    def execute(self, message: Union[discord.Message, ConsoleMessage]):
        user_id: int = None

        if isinstance(message, discord.Message):
            user_id = message.author.id
        else:
            user_id = message.user_id

        input_data = GetKPInputData(user_id)

        self._getKPUseCase.handle(input_data)