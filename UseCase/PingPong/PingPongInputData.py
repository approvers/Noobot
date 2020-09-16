class PingPongInputData:
    __slots__ = ["_content"]

    def __init__(self, content: str):
        self._content: str = content

    def get_content(self) -> str:
        return self._content