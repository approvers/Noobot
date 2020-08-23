import discord
from typing import Dict
from typing import Union

from DiscordBot.ConsoleApp.ConsoleMessage import ConsoleMessage
from UseCase.User.KP.Add.IAddKPUseCase import IAddKPUseCase
from UseCase.User.KP.Get.IGetKPUseCase import IGetKPUseCase
from DiscordBot.User.Command.IUserCommand import IUserCommand
from DiscordBot.User.Command.KP.Add.AddKPCommand import AddKPCommand
from DiscordBot.User.Command.KP.Get.GetKPCommand import GetKPCommand



class UserController:
    def __init__(
        self, 
        add_KP_useCase: IAddKPUseCase,
        get_KP_useCase: IGetKPUseCase
    ):
        self._commands: Dict[str, IUserCommand] = {
            "addKP" : AddKPCommand(add_KP_useCase),
            "getKP" : GetKPCommand(get_KP_useCase)
        }

    def on_message(self, message: Union[discord.Message, ConsoleMessage]):
        if (
            type(message) is discord.Message
            and message.author.bot
        ):
            return
        
        self._commands["addKP"].execute(message)
        
        command = message.content.strip()
        
        if command == "getKP":
            self._commands["getKP"].execute(message)
            return