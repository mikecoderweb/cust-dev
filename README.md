# Qiziqish aniqlash platformasi (website + Telegram bot)

## Papka tuzilishi
- `bot.py` — Telegram bot (Python, aiogram)
- `data.json` — savollar va natijalar (bot ham, sayt ham shundan oladi)
- `site/index.html` — website (tayyor)
- `tools/build_site.py` — `data.json` o'zgarsa saytni qayta yaratadi
- `render.yaml` — Render uchun sozlama (bot + sayt)
- `requirements.txt` — Python kutubxonalari

## Kompyuterda sinash
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export BOT_TOKEN="tokeningiz"
python bot.py
```
Saytni ko'rish: `site/index.html` ni brauzerda oching.

## GitHub'ga yuklash
1. github.com → New repository → **Private** → Create.
2. "uploading an existing file" bosing va shu papka ichidagi fayllarni sudrab tashlang (`.venv` papkasini yuklamang!) → Commit.

## Render'ga joylash
1. render.com → New → **Blueprint** → GitHub repo'ni tanlang.
2. `BOT_TOKEN` so'ralganda BotFather tokenini kiriting.
3. Apply bosing. Bot (Background Worker) va sayt (Static Site) birga yaratiladi.

Tokenni hech qachon GitHub'ga yozmang. Mac'dagi botni to'xtating (`Ctrl+C`), aks holda `Conflict` xatosi chiqadi.
