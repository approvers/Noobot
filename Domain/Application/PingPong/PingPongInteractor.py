from UseCase.PingPong.IPingPongUseCase import IPingPongUseCase
from UseCase.PingPong.PingPongInputData import PingPongInputData
from UseCase.PingPong.IPingPongPresenter import IPingPongPresenter
from UseCase .PingPong.PingPongOutputData import PingPongOutputData



class PingPongInteractor(IPingPongUseCase):
    __slots__ = ["_presenter"]

    def __init__(self, presenter: IPingPongPresenter):
        self._presenter: IPingPongPresenter = presenter

    def handle(self, input_data: PingPongInputData):
        if input_data.getContent() != "ping":
            return

        output_data = PingPongOutputData("pong")
        self._presenter.complete(output_data)
