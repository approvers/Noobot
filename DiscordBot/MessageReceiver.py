import discord
from DiscordBot.Controller.PingPong import PingPong



class MessageReceiver:
    __slots__ = ["_ping_pong"]


    def __init__(self, ping_pong: PingPong):
        self._ping_pong: PingPong = ping_pong

    def receive(self, message: discord.Message):
        self._ping_pong.input(message)