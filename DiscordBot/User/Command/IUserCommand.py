from abc import ABCMeta, abstractmethod
import discord
from typing import Union

from DiscordBot.ConsoleApp.ConsoleMessage import ConsoleMessage



class IUserCommand(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, message: Union[discord.Message, ConsoleMessage]):
        pass