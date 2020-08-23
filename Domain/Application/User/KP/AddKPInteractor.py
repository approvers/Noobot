from Domain.Domain.User.User import User
from Domain.Domain.User.IUserRepository import IUserRepository
from UseCase.User.KP.Add.IAddKPUseCase import IAddKPUseCase
from UseCase.User.KP.Add.AddKPInputData import AddKPInputData



class AddKPInteractor(IAddKPUseCase):
    def __init__(self, user_pepo: IUserRepository):
        self._user_pepo = user_pepo


    def handle(self, input_data: AddKPInputData):
        user_id = input_data.get_user_id()
        user: User = self._user_pepo.get_user(user_id)
        
        if user is None:
            user = User()
            
        KP = user.get_KP()
        user.set_KP(KP + 1)
        
        self._user_pepo.set_user(user_id, user)