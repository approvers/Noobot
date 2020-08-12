class KasuUser:
    def __init__(self, user_id: int):
        self._user_id: int = user_id
        self._kasu_coef: int = 0

    def get_user_id(self) -> int:
        return self._user_id

    def get_kasu_coef(self) -> int:
        return self._kasu_coef

    def set_kasu_coef(self, kasu_coef: int):
        self._kasu_coef = kasu_coef
        return self._kasu_coef