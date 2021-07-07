from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"- **هذا البوت لا يدعم قوائم التشغيل حاليا**\n- **فقط ارسل رابط الفيديو او الاغنية المراد تحميلها**"
    await message.reply_text(helptxt)