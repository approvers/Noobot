import discord



class GetKPInputData:
    def __init__(self, user_id: int):
        self._user_id: int = user_id

    def get_user_id(self) -> int:
        return self._user_id