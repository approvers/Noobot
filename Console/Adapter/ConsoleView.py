from Console.Adapter.ConsoleViewModel import ConsoleViewModel



class ConsoleView:
    @staticmethod
    def print(view_model: ConsoleViewModel):
        text = view_model.get_text()
        print(
            "--------\n"\
            f"{text}\n"\
            "--------\n"
        )
