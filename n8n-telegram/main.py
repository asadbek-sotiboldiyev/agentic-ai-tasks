import asyncio
import logging

import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "TOKEN"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply("Hello!")


@dp.message()
async def handle_message(message: types.Message):
    n8n_url = "http://localhost:5678/webhook-test/7b7fe729-2e7e-43fe-a1ac-6aeb01ab4a5a"
    payload = {"message": message.text}
    response = requests.post(n8n_url, json=payload)
    print(response.json())
    await message.answer(response.json())


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
