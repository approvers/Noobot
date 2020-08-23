from abc import ABCMeta, abstractmethod
from typing import Optional

from Domain.Domain.User.User import User



class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def set_user(self, user_id: int, user: User):
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        pass