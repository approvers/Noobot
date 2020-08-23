from abc import ABCMeta, abstractmethod

from UseCase.User.KP.Get.GetKPOutputData import GetKPOutputData



class IGetKPPresenter(metaclass=ABCMeta):
    @abstractmethod
    def complete(self, output_data: GetKPOutputData):
        pass