from Domain.Domain.KasuUser import KasuUser
from Domain.Domain.KasuUserList import KasuUserList
from UseCase.KasuUser.KasuCoefficient.IAddKasuCoefUserCase import IAddKasuCoefUserCase
from UseCase.KasuUser.KasuCoefficient.AddKasuCoefInputData import AddKasuCoefInputData



class KasuCoefficientInteractor(IAddKasuCoefUserCase):
    def __init__(self):
        self._user_list = KasuUserList()


    def handle(self, input_data: AddKasuCoefInputData):
        user_id = input_data.get_user_id()
        user: KasuUser = self._user_list.get_user(user_id)
        
        if user is None:
            user = KasuUser(user_id)
            
        kasu_coef = user.get_kasu_coef()
        user.set_kasu_coef(kasu_coef + 1)

        self._user_list.set_user(user)