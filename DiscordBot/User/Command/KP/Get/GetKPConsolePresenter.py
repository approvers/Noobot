import discord

from DiscordBot.ConsoleApp.ConsoleView import ConsoleView
from DiscordBot.ConsoleApp.ConsoleViewMessageModel import ConsoleViewMessageModel
from UseCase.User.KP.Get.IGetKPPresenter import IGetKPPresenter
from UseCase.User.KP.Get.GetKPOutputData import GetKPOutputData



class GetKPConsolePresenter(IGetKPPresenter):
    def __init__(self):
        self._view: ConsoleView = ConsoleView()
        
    def complete(self, output_data: GetKPOutputData):
        KP: int = output_data.get_KP()
        content = "KP: {}".format(KP)

        model: ConsoleViewMessageModel = ConsoleViewMessageModel(content)

        self._view.printMessage(model)