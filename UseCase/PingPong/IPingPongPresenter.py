from abc import ABCMeta, abstractmethod

from UseCase.PingPong.PingPongOutputData import PingPongOutputData



class IPingPongPresenter(metaclass=ABCMeta):
    @abstractmethod
    def complete(self, output_data: PingPongOutputData):
        pass