import asyncio
import logging.config
import os

from bojango.core.bot import BojangoBotConfig, BojangoBot
from dotenv import load_dotenv


load_dotenv()

config = BojangoBotConfig(
    api_token=os.getenv('TELEGRAM_BOT_API_TOKEN'),
    handlers_modules=[
        'handlers.commands',
        'handlers.callback.screens',
    ]
)


async def main():
    bot = BojangoBot(config)
    try:
        await bot.start()
    finally:
        await bot.stop()


if __name__ == '__main__':
    asyncio.run(main())