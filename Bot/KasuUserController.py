import discord

from Domain.Domain.KasuUserList import KasuUserList
from UseCase.KasuUser.KasuCoefficient.IAddKasuCoefUserCase import IAddKasuCoefUserCase
from UseCase.KasuUser.KasuCoefficient.AddKasuCoefInputData import AddKasuCoefInputData



class KasuUserController:
    def __init__(
        self, 
        add_coef_use_case: IAddKasuCoefUserCase
    ):
        self._add_coef_use_case = add_coef_use_case

    async def on_message(self, message: discord.Message):
        if not message.author.bot:
            self.add_kasu_coef(message)
    
    def add_kasu_coef(self, message: discord.Message):
        input_data = AddKasuCoefInputData(
            message.author.id,
            message.content
        )
        
        self._add_coef_use_case.handle(input_data)