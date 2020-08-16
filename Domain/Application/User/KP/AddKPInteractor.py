from Domain.Domain.User.User import User
from Domain.Domain.User.UserList import UserList
from UseCase.User.KP.AddKP.IAddKPUseCase import IAddKPUseCase
from UseCase.User.KP.AddKP.AddKPInputData import AddKPInputData



class AddKPInteractor(IAddKPUseCase):
    def __init__(self, user_list: UserList):
        self._user_list = user_list


    def handle(self, input_data: AddKPInputData):
        user_id = input_data.get_user_id()
        user: User = self._user_list.get_user(user_id)
        
        if user is None:
            user = User()
            
        KP = user.get_KP()
        user.set_KP(KP + 1)
        
        self._user_list.set_user(user_id, user)