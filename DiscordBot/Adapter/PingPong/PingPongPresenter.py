from UseCase.PingPong.IPingPongPresenter import IPingPongPresenter, PingPongOutputData
from DiscordBot.MessageView.MessageSender import MessageSender, MessageSendModel

class PingPongPresenter(IPingPongPresenter):
    __slots__ = ["_sender"]

    def __init__(self, sender: MessageSender):
        self._sender: MessageSender = sender

    def complete(self, output_data: PingPongOutputData):
        send_model = MessageSendModel(output_data.get_content())
        self._sender.push_message(send_model)