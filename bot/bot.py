import asyncio
import platform
import socket
import datetime
import os

from commands.weather import weather
from commands.notes import add_note, show_notes, show_note, delete_note, search_notes

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я Terminal Assistant 🤖")


@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Команды:\n"
        "/start\n"
        "/help\n"
        "/os\n"
        "/hostname\n"
        "/pwd\n"
        "/dt\n"
        "/weather <город>\n"
        "/notes\n"
        "/note add <текст>\n"
        "/note <id>\n"
        "/note del <id>\n"
        "/search <текст>"
    )


@dp.message(Command("os"))
async def os_handler(message: Message):
    await message.answer(platform.system())


@dp.message(Command("hostname"))
async def hostname_handler(message: Message):
    await message.answer(socket.gethostname())


@dp.message(Command("pwd"))
async def pwd_handler(message: Message):
    await message.answer(os.getcwd())


@dp.message(Command("dt"))
async def dt_handler(message: Message):
    now = datetime.datetime.now()
    await message.answer(now.strftime("%d.%m.%Y %H:%M:%S"))


@dp.message(Command("weather"))
async def weather_handler(message: Message):
    city = message.text.split(" ", 1)

    if len(city) < 2:
        await message.answer("Введите город")
    else:
        await message.answer(weather(city[1]))


@dp.message(Command("notes"))
async def notes_handler(message: Message):
    await message.answer(show_notes())


@dp.message(Command("note"))
async def note_handler(message: Message):
    parts_note = message.text.split(" ", 2)

    if len(parts_note) < 2:
        await message.answer("Введите команду заметки")

    elif parts_note[1] == "add":
        if len(parts_note) > 2:
            await message.answer(add_note(parts_note[2]))
        else:
            await message.answer("Введите текст заметки")

    elif parts_note[1] == "del":
        if len(parts_note) > 2:
            try:
                note_id = int(parts_note[2])
                await message.answer(delete_note(note_id))
            except ValueError:
                await message.answer("ID должен быть числом")
        else:
            await message.answer("Введите ID заметки")

    elif parts_note[1].isdigit():
        note_id = int(parts_note[1])
        await message.answer(show_note(note_id))

    else:
        await message.answer("Неизвестная команда заметки")


@dp.message(Command("search"))
async def search_handler(message: Message):
    parts = message.text.split(" ", 1)

    if len(parts) < 2:
        await message.answer("Введите текст для поиска")
    else:
        await message.answer(search_notes(parts[1]))


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())