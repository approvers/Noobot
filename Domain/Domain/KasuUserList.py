from typing import List
from typing import Optional

from Domain.Domain.KasuUser import KasuUser



class KasuUserList:
    def __init__(self):
        self._users: List[KasuUser] = []

    def set_user(self, user: KasuUser):
        user_id = user.get_user_id()
        for e_user in self._users:
            if e_user.get_user_id() == user_id:
                e_user = user
                return

        self._users.append(user)

    def get_user(self, user_id: int) -> Optional[KasuUser]:
        for user in self._users:
            if user.get_user_id() == user_id:
                return user

        return None