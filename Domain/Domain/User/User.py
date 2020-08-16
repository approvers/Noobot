class User:
    def __init__(self):
        self._KP: int = 0

    def get_KP(self) -> int:
        return self._KP

    def set_KP(self, KP: int):
        self._KP = KP