class AddKasuCoefInputData:
    def __init__(self, user_id: int, content: str):
        self._user_id: int = user_id
        self._content: str = content

    def get_user_id(self) -> int:
        return self._user_id

    def get_content(self) -> str:
        return self._content