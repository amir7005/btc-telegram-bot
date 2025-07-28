from flask import Flask, request
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os

app = Flask(__name__)

TOKEN = "8188240924:AAGWgj_E9A-sLhJuDQVL_LHsEovY5kV4BE4"
bot = telegram.Bot(token=TOKEN)

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.effective_chat.id
        message = update.message.text if update.message else None
        callback_data = update.callback_query.data if update.callback_query else None

        if message == "/start":
            keyboard = [
                [InlineKeyboardButton("تشخیص روند", callback_data="trend")],
                [InlineKeyboardButton("هشدار شکست", callback_data="breakout")],
                [InlineKeyboardButton("استراتژی M.Box", callback_data="mbox")],
                [InlineKeyboardButton("استراتژی NYC", callback_data="nyc")],
                [InlineKeyboardButton("حذف تاریخچه", callback_data="delete_history")],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot.send_message(chat_id=chat_id, text="یکی از گزینه‌ها رو انتخاب کن:", reply_markup=reply_markup)

        elif callback_data:
            bot.send_message(chat_id=chat_id, text=f"شما دکمه‌ی {callback_data} رو انتخاب کردید.")

        return "ok"

    return "bot running"
