import discord
from typing import Dict

from Domain.Domain.UserList import UserList
from UseCase.User.KP.IAddKPUseCase import IAddKPUseCase
from Bot.User.Command.IUserCommand import IUserCommand
from Bot.User.Command.AddKPCommand import AddKPCommand



class UserController:
    def __init__(
        self, 
        add_KP_useCase: IAddKPUseCase
    ):
        self._commands: Dict[str, IUserCommand] = {
            "addKP" : AddKPCommand(add_KP_useCase)
        }

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        
        self._commands["addKP"].execute(message)