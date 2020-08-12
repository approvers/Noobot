from abc import ABCMeta, abstractmethod

from UseCase.KasuUser.KasuCoefficient.AddKasuCoefInputData import AddKasuCoefInputData



class IAddKasuCoefUserCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input_data: AddKasuCoefInputData):
        pass