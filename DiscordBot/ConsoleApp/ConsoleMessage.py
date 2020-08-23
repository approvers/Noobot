import discord



class ConsoleMessage:
    def __init__(
        self,
        content: str,
        user_id: int
    ):
        self.content: str = content
        self.user_id: int = user_id