class ConsoleViewModel:
    __slots__ = ["_text"]

    def __init__(self, text: str):
        self._text: str = text

    def getText(self) -> str:
        return self._text