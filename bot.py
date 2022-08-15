from pyrogram import Client
from trim import trim
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply 


video_mimetype = [
    "video/x-flv",
    "video/mp4",
    "video/avi",
    "video/mkv",
    "application/x-mpegURL",
    "video/mp2t",
    "video/3gpp",
    "video/quicktime",
    "video/x-msvideo",
    "video/x-ms-wmv",
    "video/x-matroska",
    "video/webm",
    "video/x-m4v",
    "video/quicktime",
    "video/mpeg"
]

bot = Client(
    'trimmer',
    bot_token=BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins
    )

@Client.on_message((filters.video | filters.document))
async def video(bot, message):
    if message.document:
        if not message.document.mime_type in video_mimetype:
            message.reply_text("```Geçersiz Video !\nBu video dosyasına benzemiyor.```", quote=True)
            return
    try:
        ss = await bot.send_message("Başlangıç süresini yaz.\n\n örnek: `01:20:69`", reply_markup=ForceReply(True))
        s = await ss.get_reply()
        baslangic = s.text
        await ss.delete()
    except Exception as e:
        print(e)
        return await bot.send_message("hata oldu")
    try:
        dd = await bot.send_message("bitiş süresini yaz.\n\n örnek: `01:50:69`", reply_markup=ForceReply(True))
        d = await d.get_reply()
        bitis = d.text
        await dd.delete()
    except Exception as f:
        print(f)
        return await bot.send_message("hata oldu")
    await trim(message, baslangic, bitis)

bot.run()
