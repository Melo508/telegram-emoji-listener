import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = 38127971
api_hash = "8d7829de23b386a7bfef92c1f89a5f83"

async def main():
    async with TelegramClient(StringSession(), api_id, api_hash) as client:
        print("✅ Copia esto y guárdalo como STRING_SESSION en Railway:")
        print(client.session.save())

asyncio.run(main())