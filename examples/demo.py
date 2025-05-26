from pyroanimate import Animate
from pyrogram import Client

chat_id = 123

app = Client("bot")

anim = Animate(app,delay = 0.3,sync = True)
anim.add_animations("walk", ["🚶", "🏃", "🚶‍♂️"])
anim.run(chat_id, default = True, frames = None, animation_id = "walk")
