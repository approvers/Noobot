from abc import ABCMeta, abstractmethod

from UseCase.User.KP.AddKP.AddKPInputData import AddKPInputData



class IAddKPUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input_data: AddKPInputData):
        pass