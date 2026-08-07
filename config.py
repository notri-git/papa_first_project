from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

COMMANDS = [
    "/help - список команд",
    "/crypt текст - зашифровать",
    "/decrypt текст - расшифровать",
    "/os - информация о системе",
    "/hostname - имя компьютера",
    "/pwd - текущая папка",
    "/ls - список файлов",
    "/dt - дата и время",
    "/weather город - узнать погоду",
    "/note add текст - добавить заметку",
    "/note ID - показать заметку",
    "/note del ID - удалить заметку",
    "/notes - показать все заметки",
    "/search текст - поиск заметок",
    "/exit - выход"
]