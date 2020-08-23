import discord

from DiscordBot.MessageSender import MessageSender
from DiscordBot.MessageSendModel import MessageSendModel
from UseCase.User.KP.Get.IGetKPPresenter import IGetKPPresenter
from UseCase.User.KP.Get.GetKPOutputData import GetKPOutputData



class GetKPMessagePresenter(IGetKPPresenter):
    def __init__(self, sender: MessageSender):
        self._sender: MessageSender = sender
        
    def complete(self, output_data: GetKPOutputData):
        KP: int = output_data.get_KP()
        content = "KP: {}".format(KP)

        model: MessageSendModel = MessageSendModel(content)

        self._sender.push_message(model)