import discord
from UseCase.PingPong.IPingPongUseCase import IPingPongUseCase, PingPongInputData



class PingPong:
    __slots__ = ["_ping_pong_interctor"]

    def __init__(
        self,
        ping_pong_interctor: IPingPongUseCase
    ):
        self._ping_pong_interctor: IPingPongUseCase = ping_pong_interctor

    def input(self, message: discord.Message):
        input_data = PingPongInputData(message.content)
        self._ping_pong_interctor.handle(input_data)