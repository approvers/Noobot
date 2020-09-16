from Console.Adapter.PingPong.ConsolePingPong import ConsolePingPong



class ConsoleController:
    __slots__ = ["_ping_pong"]

    def __init__(
        self,
        ping_pong: ConsolePingPong
    ):
        self._ping_pong: ConsolePingPong = ping_pong

    def input(self, text: str):
        self._ping_pong.input(text)