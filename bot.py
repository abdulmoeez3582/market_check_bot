import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from main import get_BTC

telegram_bot_token = "5154256083:AAFdr9j4U-zCFo8LP-85W_TViQnkIwV9v7s"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Please Enter Your Coin with / e.g /BTC")


dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()

def BTC(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_BTC()
    for i in crypto_data:
        price = crypto_data[i]["trade_price"]
        message += f"BTC: {price:,.2f}원"

    context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("btc", BTC))
updater.start_polling()