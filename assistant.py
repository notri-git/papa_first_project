from ollama import Client

from commands.crypto import crypt
from commands.crypto import decrypt

from commands.system import os_info
from commands.system import hostname
from commands.system import pwd
from commands.system import ls
from commands.system import dt

from commands.weather import weather

from commands.notes import add_note
from commands.notes import show_notes
from commands.notes import show_note
from commands.notes import delete_note
from commands.notes import search_notes

from config import COMMANDS
from config import OLLAMA_API_KEY
from config import OLLAMA_MODEL


class Assistant:

    def process_message(self, message):
        message = message.strip()

        if message == "":
            return ""

        parts = message.split(" ", 1)

        command = parts[0].lower()

        if len(parts) > 1:
            text = parts[1]
        else:
            text = ""

        if command.startswith("/"):
            return self.process_command(command, text)

        return self.ask_ai(message)

    def process_command(self, command, text):

        if command == "/help":
            return "\n".join(COMMANDS)

        elif command == "/exit":
            return "Пока!"

        elif command == "/crypt":
            if text == "":
                return "Введите текст"

            return crypt(text)

        elif command == "/decrypt":
            if text == "":
                return "Введите текст"

            return decrypt(text)

        elif command == "/os":
            return os_info()

        elif command == "/hostname":
            return hostname()

        elif command == "/pwd":
            return pwd()

        elif command == "/ls":
            return ls()

        elif command == "/dt":
            return dt()

        elif command == "/weather":
            if text == "":
                return "Введите город"

            return weather(text)

        elif command == "/note":
            parts_note = text.split(" ", 1)

            if text == "":
                return "Введите команду заметки"

            elif parts_note[0] == "add":
                if len(parts_note) > 1:
                    return add_note(parts_note[1])

                return "Введите текст заметки"

            elif parts_note[0] == "del":
                if len(parts_note) > 1:
                    try:
                        note_id = int(parts_note[1])
                        return delete_note(note_id)

                    except ValueError:
                        return "ID должен быть числом"

                return "Введите ID заметки"

            elif parts_note[0].isdigit():
                note_id = int(parts_note[0])
                return show_note(note_id)

            return "Неизвестная команда заметки"

        elif command == "/notes":
            return show_notes()

        elif command == "/search":
            if text == "":
                return "Введите текст для поиска"

            return search_notes(text)

        return "Команда не найдена. Введите /help"

    def ask_ai(self, message):

        try:
            client = Client(
                host="https://ollama.com",
                headers={
                    "Authorization": "Bearer " + OLLAMA_API_KEY
                }
            )

            response = client.chat(
                model=OLLAMA_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )

            return response["message"]["content"]

        except Exception:
            return "AI отдыхает, попробуй позже"

    def output(self, result):
        pass