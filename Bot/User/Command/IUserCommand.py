from abc import ABCMeta, abstractmethod
import discord



class IUserCommand(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, message: discord.Message):
        pass