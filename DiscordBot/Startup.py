from DiscordBot.MessageReceiver import MessageReceiver
from DiscordBot.User.UserController import UserController

from DiscordBot.InMemoryUserList import InMemoryUserList
from DiscordBot.MessageSender import MessageSender

from Domain.Application.User.KP.AddKPInteractor import AddKPInteractor
from Domain.Application.User.KP.GetKPInteractor import GetKPInteractor
from DiscordBot.User.Command.KP.Get.GetKPConsolePresenter import GetKPConsolePresenter
from DiscordBot.User.Command.KP.Get.GetKPMessagePresenter import GetKPMessagePresenter



class Startup:
    @staticmethod
    def console_receiver() -> MessageReceiver:
        user_repo: InMemoryUserList = InMemoryUserList()
        sender: MessageSender = MessageSender()
        
        
        user_controller = UserController(
            AddKPInteractor(user_repo),
            GetKPInteractor(
                user_repo,
                GetKPConsolePresenter()
            )
        )
        
        return MessageReceiver(
            sender,
            user_controller
        )
        
    @staticmethod
    def message_receiver() -> MessageReceiver:
        user_repo: InMemoryUserList = InMemoryUserList()
        sender: MessageSender = MessageSender()
        
        user_controller = UserController(
            AddKPInteractor(user_repo),
            GetKPInteractor(
                user_repo,
                GetKPMessagePresenter(sender)
            )
        )
        
        return MessageReceiver(
            sender,
            user_controller
        )