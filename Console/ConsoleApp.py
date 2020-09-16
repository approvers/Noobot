from Console.Adapter.ConsoleController import ConsoleController
from Domain.Application.PingPong.PingPongInteractor import PingPongInteractor
from Console.Adapter.PingPong.ConsolePingPong import ConsolePingPong
from Console.Adapter.PingPong.PingPongConsolePresenter import PingPongConsolePresenter



def console_run():
    controller = ConsoleController(
        ConsolePingPong(PingPongInteractor(PingPongConsolePresenter()))
    )

    while(True):
        text: str = input()

        if text == "exit":
            return

        controller.input(text)