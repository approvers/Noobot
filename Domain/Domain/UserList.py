from typing import Dict
from typing import Optional

from Domain.Domain.User import User



class UserList:
    def __init__(self):
        self._users: Dict[int, User] = {}

    def set_user(self, user_id: int, user: User):
        self._users[user_id] = user

    def get_user(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)