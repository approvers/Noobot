from Domain.Domain.User.User import User
from Domain.Domain.User.UserList import UserList
from UseCase.User.KP.GetKP.IGetKPUseCase import IGetKPUseCase
from UseCase.User.KP.GetKP.GetKPInputData import GetKPInputData



class GetKPInteractor(IGetKPUseCase):
    def __init__(self, user_list: UserList):
        self._user_list = user_list


    def handle(self, input_data: GetKPInputData) -> int:
        user_id = input_data.get_user_id()
        user = self._user_list.get_user(user_id)

        if user is None:
            return 0

        return user.get_KP()