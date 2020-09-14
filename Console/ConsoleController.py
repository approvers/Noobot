from UseCase.PingPong.IPingPongUseCase import IPingPongUseCase, PingPongInputData



class ConsoleController:
    __slots__ = ["_ping_pong_interctor"]

    def __init__(
        self,
        ping_pong_interctor: IPingPongUseCase
    ):
        self._ping_pong_interctor: IPingPongUseCase = ping_pong_interctor

    def input(self, text: str):
        input_data = PingPongInputData(text)
        self._ping_pong_interctor.handle(input_data)