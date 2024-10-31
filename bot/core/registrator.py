from pyrogram import Client
from bot.utils import logger

async def register_sessions() -> None:
    session_name = input('\nEnter the session ID (press Enter to exit): ')

    if not session_name:
        return None

    session = Client(
        name=session_name,
        workdir="sessions/"
    )

    async with session:
        user_data = await session.get_me()

    logger.info(f'Session added successfully @{user_data.username} | {user_data.first_name} {user_data.last_name}')