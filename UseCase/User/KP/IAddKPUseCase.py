from abc import ABCMeta, abstractmethod

from UseCase.User.KP.AddKPInputData import AddKPInputData



class IAddKPUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input_data: AddKPInputData):
        pass