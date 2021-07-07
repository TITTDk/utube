from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("• Channel ", url="https://t.me/ILOIOIL")],
    ])
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("• Dev ", url="https://t.me/TITTD")],
        ])
    welcomed = f"**🏃 ┇  مرحبا بك : <b>{message.from_user.first_name}</b>\n\nيمكنك تحميل من يوتيوب بأستخدام البوت .\nارسل رابط الاغنية فقـط -- -- -- -- -- -- -- -- -- -- -- -- -- --**"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation