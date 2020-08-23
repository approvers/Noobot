import discord


from Domain.Domain.User.User import User
from Domain.Domain.User.IUserRepository import IUserRepository
from UseCase.User.KP.Get.IGetKPUseCase import IGetKPUseCase
from UseCase.User.KP.Get.GetKPInputData import GetKPInputData
from UseCase.User.KP.Get.IGetKPPresenter import IGetKPPresenter
from UseCase.User.KP.Get.GetKPOutputData import GetKPOutputData



class GetKPInteractor(IGetKPUseCase):
    def __init__(self, user_repo: IUserRepository, presenter: IGetKPPresenter):
        self._user_repo: IUserRepository = user_repo
        self._presenter: IGetKPPresenter = presenter


    def handle(self, input_data: GetKPInputData):
        user_id = input_data.get_user_id()
        user = self._user_repo.get_user(user_id)
        KP: int = user.get_KP()

        output_data = GetKPOutputData(KP)

        self._presenter.complete(output_data)