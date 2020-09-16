class ConsoleViewModel:
    __slots__ = ["_text"]

    def __init__(self, text: str):
        self._text: str = text

    def get_text(self) -> str:
        return self._text