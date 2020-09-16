import discord
from DiscordBot.Adapter.PingPong import PingPong
from DiscordBot.MessageView.MessageSender import MessageSender



class MessageReceiver:
    __slots__ = ["_sender", "_ping_pong"]


    def __init__(self, sender: MessageSender, ping_pong: PingPong):
        self._sender: MessageSender = sender
        self._ping_pong: PingPong = ping_pong

    async def receive(self, message: discord.Message):
        self._ping_pong.input(message)

        await self._sender.send(message.channel)