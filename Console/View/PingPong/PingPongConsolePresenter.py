from UseCase.PingPong.IPingPongPresenter import IPingPongPresenter
from UseCase.PingPong.PingPongOutputData import PingPongOutputData
from Console.View.ConsoleView import ConsoleView
from Console.View.ConsoleViewModel import ConsoleViewModel


class PingPongConsolePresenter(IPingPongPresenter):
    def complete(self, output_data: PingPongOutputData):
        view_model = ConsoleViewModel(output_data.getContent())
        ConsoleView.print(view_model)