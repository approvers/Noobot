from Console.View.ConsoleViewModel import ConsoleViewModel



class ConsoleView:
    @staticmethod
    def print(view_model: ConsoleViewModel):
        text = view_model.getText()
        print(
            "--------\n"\
            f"{text}\n"\
            "--------\n"
        )
