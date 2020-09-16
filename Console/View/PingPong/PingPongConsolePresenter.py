from UseCase.PingPong.IPingPongPresenter import IPingPongPresenter, PingPongOutputData
from Console.View.ConsoleView import ConsoleView, ConsoleViewModel


class PingPongConsolePresenter(IPingPongPresenter):
    def complete(self, output_data: PingPongOutputData):
        view_model = ConsoleViewModel(output_data.get_content())
        ConsoleView.print(view_model)