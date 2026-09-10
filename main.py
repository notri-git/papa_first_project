from console_assistant import ConsoleAssistant


assistant = ConsoleAssistant()

print("ДОБРО ПОЖАЛОВАТЬ!")
print("Команды:")

result = assistant.process_message("/help")
assistant.output(result)


while True:
    vvod = input()

    result = assistant.process_message(vvod)

    if result != "":
        assistant.output(result)

    if vvod.strip().lower() == "/exit":
        break