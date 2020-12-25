from telethon import events
from csi import csi

@csi.on(events.NewMessage(pattern="^.ping", outgoing=True))
async def _(hehe):
    await hehe.edit("Pong")
