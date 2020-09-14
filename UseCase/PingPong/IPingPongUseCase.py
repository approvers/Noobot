from abc import ABCMeta, abstractmethod

from UseCase.PingPong.PingPongInputData import PingPongInputData



class IPingPongUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input_data: PingPongInputData):
        pass