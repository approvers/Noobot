from DiscordBot.ConsoleApp.ConsoleViewMessageModel import ConsoleViewMessageModel



class ConsoleView:
    def printMessage(self, model: ConsoleViewMessageModel):
        print("[CONTENT]\n{}\n".format(model.content))