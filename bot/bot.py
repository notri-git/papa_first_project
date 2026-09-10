import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from dotenv import load_dotenv

from telegram_assistant import TelegramAssistant


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()
assistant = TelegramAssistant()


@dp.message()
async def message_handler(message: Message):
    result = assistant.process_message(message.text)

    if result != "":
        await message.answer(assistant.output(result))


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())