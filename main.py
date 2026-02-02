import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
string_sess = os.environ.get("STRING_SESSION")

ORIGENES = [-1001978284886]
DESTINO = -1003829930906

KEYWORDS = ["Approved.!! ✅", "Approved ✅"]

client = TelegramClient(StringSession(string_sess), api_id, api_hash)

def contiene_aprobado(texto):
    return any(k in texto for k in KEYWORDS) if texto else False

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