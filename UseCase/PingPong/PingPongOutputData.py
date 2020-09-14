class PingPongOutputData:
    __slots__ = ["_content"]

    def __init__(self, content: str):
        self._content: str = content
    
    def getContent(self) -> str:
        return self._content