from assistant import Assistant


class ConsoleAssistant(Assistant):

    def output(self, result):
        print(result)