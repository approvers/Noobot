from Console.ConsoleController import ConsoleController
from Domain.Application.PingPong.PingPongInteractor import PingPongInteractor
from Console.View.PingPong.PingPongConsolePresenter import PingPongConsolePresenter



def console_run():
    controller = ConsoleController(
        PingPongInteractor(PingPongConsolePresenter())
    )

    while(True):
        text: str = input()

        if text == "exit":
            return

        controller.input(text)