import asyncio
from telethon import TelegramClient, events

api_id = 38127971
api_hash = "8d7829de23b386a7bfef92c1f89a5f83"

ORIGENES = [-1001978284886]
DESTINO = -1003829930906

KEYWORDS = [
    "Approved.!! ✅",
    "Approved ✅"
]

client = TelegramClient("session", api_id, api_hash)

def contiene_aprobado(texto):
    if not texto:
        return False
    return any(k in texto for k in KEYWORDS)

@client.on(events.NewMessage(chats=ORIGENES))
@client.on(events.MessageEdited(chats=ORIGENES))
async def handler(event):
    texto = event.message.text
    if contiene_aprobado(texto):
        await client.send_message(DESTINO, texto)
        print("✅ Mensaje reenviado")

async def main():
    await client.start()
    print("🟢 Listener activo")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())