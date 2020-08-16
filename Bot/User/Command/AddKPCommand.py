import discord

from Bot.User.Command.IUserCommand import IUserCommand
from UseCase.User.KP.AddKP.IAddKPUseCase import IAddKPUseCase
from UseCase.User.KP.AddKP.AddKPInputData import AddKPInputData



class AddKPCommand(IUserCommand):
    def __init__(self, addKPUseCase: IAddKPUseCase):
        self._addKPUseCase = addKPUseCase

    def execute(self, message: discord.Message):
        user_id = message.author.id
        input_data = AddKPInputData(user_id)

        self._addKPUseCase.handle(input_data)