
import telegram
import requests
import locale
from telegram.ext import Updater
from telegram.ext import CommandHandler

telegram_bot_token = "5154256083:AAFdr9j4U-zCFo8LP-85W_TViQnkIwV9v7s"

locale.setlocale(locale.LC_ALL, 'Korean')

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="환영하다")


dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()

def BTC(update, context):
    chat_id = update.effective_chat.id

    crypto_data = requests.get(
        "https://api.upbit.com/v1/ticker?markets=KRW-BTC").json()


    tradeprice = []
    changeprice = []
    change = []
    a = "🔴"
    b = "🔵"
    for i in crypto_data:
         tradeprice = i["trade_price"]
         changeprice = i["signed_change_rate"]
         change = i["change"]
         if change == "FALL":
            message = f"BTC: {tradeprice:.0f}원\n24h:{a} {changeprice:.3f}%\n"
         else:
            message = f"BTC: {tradeprice:.0f}원\n24h:{b} {changeprice:.3f}%\n"

         context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("btc", BTC))
updater.start_polling()

def bitcoin (update, context):
    chat_id = update.effective_chat.id

    crypto_data = requests.get(
        "https://api.upbit.com/v1/ticker?markets=KRW-BTC").json()

    tradeprice = []
    changeprice = []
    change = []
    a = "🔴"
    b = "🔵"
    for i in crypto_data:
         tradeprice = i["trade_price"]
         changeprice = i["signed_change_rate"]
         change = i["change"]
         if change == "FALL":
            message = f"BTC: {tradeprice:.0f}원\n24h:{a} {changeprice:.3f}%\n"
         else:
            message = f"BTC: {tradeprice:.0f}원\n24h:{b} {changeprice:.3f}%\n"
         context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("bitcoin", bitcoin))
updater.start_polling()

def ETH (update, context):
    chat_id = update.effective_chat.id

    crypto_data = requests.get(
        "https://api.upbit.com/v1/ticker?markets=KRW-ETH").json()

    tradeprice = []
    changeprice = []
    change = []
    a = "🔴"
    b = "🔵"
    for i in crypto_data:
         tradeprice = i["trade_price"]
         changeprice = i["signed_change_rate"]
         change = i["change"]
         if change == "FALL":
            message = f"ETH: {tradeprice:.0f}원\n24h:{a} {changeprice:.3f}%\n"
         else:
            message = f"ETH: {tradeprice:.0f}원\n24h:{b} {changeprice:.3f}%\n"
         context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("ETH", ETH))
updater.start_polling()

def Etherium (update, context):
    chat_id = update.effective_chat.id

    crypto_data = requests.get(
        "https://api.upbit.com/v1/ticker?markets=KRW-ETH").json()

    tradeprice = []
    changeprice = []
    change = []
    a = "🔴"
    b = "🔵"
    for i in crypto_data:
         tradeprice = i["trade_price"]
         changeprice = i["signed_change_rate"]
         change = i["change"]
         if change == "FALL":
            message = f"ETH: {tradeprice:.0f}원\n24h:{a} {changeprice:.3f}%\n"
         else:
            message = f"ETH: {tradeprice:.0f}원\n24h:{b} {changeprice:.3f}%\n"
         context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("Ethereum",Etherium ))
updater.start_polling()