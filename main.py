from commands.crypto import crypt
from commands.crypto import decrypt

from bot.bot import main

from commands.system import os_info
from commands.system import hostname
from commands.system import pwd
from commands.system import ls
from commands.system import dt

from commands.weather import weather

from config import COMMANDS
from config import HELP_COMMANDS

print("ДОБРО ПОЖАЛОВАТЬ!")
print("Команды:", ", ".join(COMMANDS))
from commands.notes import add_note
from commands.notes import show_notes
from commands.notes import show_note
from commands.notes import delete_note
from commands.notes import search_notes

from config import COMMANDS


if __name__ == "__main__":
    main()

print("ДОБРО ПОЖАЛОВАТЬ!")
print("Команды:")

for command in COMMANDS:
    print(command)


while True:
    vvod = input().strip()

    if vvod == "":
        continue

    parts = vvod.split(" ", 1)

    komanda = parts[0].lower()

    if len(parts) > 1:
        tekst = parts[1]
    else:
        tekst = ""

    if komanda == "/help":
        for command in HELP_COMMANDS:
        for command in COMMANDS:
            print(command)

    elif komanda == "/exit":
        print("Пока!")
        break

    elif komanda == "/crypt":
        if tekst == "":
            print("Введите текст")
        else:
            print(crypt(tekst))

    elif komanda == "/decrypt":
        if tekst == "":
            print("Введите текст")
        else:
            print(decrypt(tekst))

    elif komanda == "/os":
        os_info()

    elif komanda == "/hostname":
        hostname()

    elif komanda == "/pwd":
        pwd()

    elif komanda == "/ls":
        ls()

    elif komanda == "/dt":
        dt()

    elif komanda == "/weather":
        if tekst == "":
            print("Введите город")
        else:
            weather(tekst)

    elif komanda == "/note":
        parts_note = tekst.split(" ", 1)

        if len(parts_note) == 0:
            print("Введите команду заметки")

        elif parts_note[0] == "add":
            if len(parts_note) > 1:
                add_note(parts_note[1])
            else:
                print("Введите текст заметки")

        elif parts_note[0] == "del":
            if len(parts_note) > 1:
                try:
                    note_id = int(parts_note[1])
                    delete_note(note_id)
                except ValueError:
                    print("ID должен быть числом")
            else:
                print("Введите ID заметки")

        elif parts_note[0].isdigit():
            note_id = int(parts_note[0])
            show_note(note_id)

        else:
            print("Неизвестная команда заметки")

    elif komanda == "/notes":
        show_notes()

    elif komanda == "/search":
        if tekst == "":
            print("Введите текст для поиска")
        else:
            search_notes(tekst)

    else:
        print("Команда не найдена. Введите /help")