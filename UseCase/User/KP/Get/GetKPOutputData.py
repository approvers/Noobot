import discord



class GetKPOutputData:
    def __init__(self, KP: int):
        self._KP: int = KP

    def get_KP(self) -> int:
        return self._KP