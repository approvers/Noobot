from DiscordBot.Client import Client

from DiscordBot.MessageReceiver import MessageReceiver
from DiscordBot.User.UserController import UserController

from DiscordBot.ConsoleApp.ConsoleMessage import ConsoleMessage

from DiscordBot.InMemoryUserList import InMemoryUserList
from DiscordBot.MessageSender import MessageSender

from Domain.Application.User.KP.AddKPInteractor import AddKPInteractor
from Domain.Application.User.KP.GetKPInteractor import GetKPInteractor
from DiscordBot.User.Command.KP.Get.GetKPConsolePresenter import GetKPConsolePresenter
from DiscordBot.User.Command.KP.Get.GetKPMessagePresenter import GetKPMessagePresenter



class Startup:
    @staticmethod
    def console_run():
        user_repo: InMemoryUserList = InMemoryUserList()
        sender: MessageSender = MessageSender()
        
        
        user_controller = UserController(
            AddKPInteractor(user_repo),
            GetKPInteractor(
                user_repo,
                GetKPConsolePresenter()
            )
        )
        
        receiver: MessageReceiver = MessageReceiver(
            sender,
            user_controller
        )

        user_id: int = 0

        while True:
            content:str  = input()
            message = ConsoleMessage(content, user_id)
            receiver.input(message)
        

    @staticmethod
    def client_run():
        user_repo: InMemoryUserList = InMemoryUserList()
        sender: MessageSender = MessageSender()
        
        user_controller = UserController(
            AddKPInteractor(user_repo),
            GetKPInteractor(
                user_repo,
                GetKPMessagePresenter(sender)
            )
        )
        
        client = Client(
            MessageReceiver(
                sender,
                user_controller
            )
        )

        client.run()