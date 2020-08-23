import discord
from typing import List

from DiscordBot.MessageSendModel import MessageSendModel


class MessageSender:
    def __init__(self):
        self._model_stack: List[MessageSendModel] = []

    def push_message(self, model: MessageSendModel):
        self._model_stack.append(model)

    async def send(self, channel: discord.TextChannel):
        while len(self._model_stack) > 0:
            model = self._model_stack.pop(0)

            await channel.send(
                model.content,
                tts = model.tts,
                embed = model.embed,
                file = model.file,
                files = model.files,
                delete_after = model.delete_after,
                nonce = model.nonce,
                allowed_mentions = model.allowed_mentions
            )