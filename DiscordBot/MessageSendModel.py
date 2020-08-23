import discord
from typing import List



class MessageSendModel:
    def __init__(
        self,
        content:            str                     = None,
        *,
        tts:                bool                    = False,
        embed:              discord.Embed           = None, 
        file:               discord.File            = None, 
        files:              List[discord.File]      = None, 
        delete_after:       float                   = None, 
        nonce:              int                     = None,
        allowed_mentions:   int                     = None
    ):
        self.content: str = content
        self.tts: bool = tts
        self.embed: discord.Embed = embed
        self.file: discord.File = file
        self.files: List[discord.File] = files
        self.delete_after: float = delete_after
        self.nonce: int = nonce
        self.allowed_mentions: discord.AllowedMentions = allowed_mentions