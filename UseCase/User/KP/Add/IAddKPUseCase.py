from abc import ABCMeta, abstractmethod

from UseCase.User.KP.Add.AddKPInputData import AddKPInputData



class IAddKPUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input_data: AddKPInputData):
        pass