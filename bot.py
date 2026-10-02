"""Qiziqish aniqlash boti (aiogram 3).
Ishga tushirish:  pip install aiogram
                  export BOT_TOKEN="@BotFather bergan token"
                  python bot.py          (data.json shu papkada bo'lsin)
"""
import asyncio, json, os, random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardButton as Btn, InlineKeyboardMarkup as Kb, Message

D = json.load(open(os.path.join(os.path.dirname(__file__), "data.json"), encoding="utf-8"))
dp, users = Dispatcher(), {}

def age_kb():
    return Kb(inline_keyboard=[[Btn(text=f"{a['label']} ({a['sub']})", callback_data=f"age:{i}")] for i, a in enumerate(D["ages"])])

def scale_kb():
    return Kb(inline_keyboard=[[Btn(text=str(n), callback_data=f"a:{n}") for n in range(1, 6)]])

@dp.message(CommandStart())
async def start(m: Message):
    await m.answer("Salom! 👋 Bu test qiziqish va moyilligingizni aniqlaydi (taxminan 5 daqiqa).\n\nYoshingizni tanlang:", reply_markup=age_kb())

@dp.callback_query(F.data.startswith("age:"))
async def pick_age(c: CallbackQuery):
    a = D["ages"][int(c.data[4:])]
    qs = [(t, q) for t, lst in D["q"][a["set"]].items() for q in lst]
    random.shuffle(qs)
    users[c.from_user.id] = {"who": a["who"], "qs": qs, "i": 0, "sc": {t: 0 for t in D["types"]}}
    await c.message.answer("Har bir gapga 1 dan 5 gacha baho bering:\n1 = umuman yoqmaydi, 5 = juda yoqadi")
    await ask(c.message, c.from_user.id)
    await c.answer()

async def ask(msg: Message, uid: int):
    u = users[uid]
    if u["i"] >= len(u["qs"]):
        return await result(msg, uid)
    await msg.answer(f"{u['i']+1}/{len(u['qs'])}\n\n{u['who']} {u['qs'][u['i']][1]}", reply_markup=scale_kb())

@dp.callback_query(F.data.startswith("a:"))
async def answer(c: CallbackQuery):
    u = users.get(c.from_user.id)
    if not u:
        return await c.answer("Boshlash uchun /start bosing")
    u["sc"][u["qs"][u["i"]][0]] += int(c.data[2:])
    u["i"] += 1
    await c.message.edit_reply_markup(reply_markup=None)
    await ask(c.message, c.from_user.id)
    await c.answer()

async def result(msg: Message, uid: int):
    top = sorted(users[uid]["sc"].items(), key=lambda x: -x[1])[:3]
    out = "✅ Natijangiz — eng yuqori 3 yo'nalish:\n"
    for k, (t, s) in enumerate(top, 1):
        i = D["types"][t]
        out += f"\n{k}. {i['n']} ({s}/15)\n{i['d']}\nFanlar: {i['s']}\nKasblar: {i['p']}\n"
    out += "\n⚠️ Bu taqdir emas, moyillik ko'rsatkichi. Qaror qabul qilishda boshqa omillarni ham hisobga oling.\n\nQayta topshirish: /start"
    await msg.answer(out)
    users.pop(uid, None)

async def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise SystemExit("BOT_TOKEN topilmadi. Tokenni muhit o'zgaruvchisiga qo'ying.")
    await dp.start_polling(Bot(token))

if __name__ == "__main__":
    asyncio.run(main())
