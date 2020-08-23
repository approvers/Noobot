from abc import ABCMeta, abstractmethod

from UseCase.User.KP.Get.GetKPInputData import GetKPInputData



class IGetKPUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input_data: GetKPInputData) -> int:
        pass