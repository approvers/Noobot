from DiscordBot.Client import Client
from Console.ConsoleApp import console_run


if __name__ == "__main__":
    if __debug__:
        console_run()
    else:
        Client().run()