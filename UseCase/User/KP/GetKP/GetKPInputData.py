import discord



class GetKPInputData:
    def __init__(self, channle: discord.TextChannel, user_id: int):
        self._channle: discord.TextChannel = channle
        self._user_id: int = user_id

    def get_channle(self) -> discord.TextChannel:
        return self._channle

    def get_user_id(self) -> int:
        return self._user_id