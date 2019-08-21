from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from settings import token


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

def greeting(bot, update):
    msg = "Bots is comming!!!"
    logging.info(msg)
    update.message.reply_text(msg)

def talk_to_me(bot, update):
    user_msg = f"Привет {update.message.chat.first_name}!! \nТы написал: {update.message.text}"
    logging.info(f'User: {update.message.chat.username}, Chat id: {update.message.chat.id}, Message: {update.message.text}')
    update.message.reply_text(user_msg)


def main():
    bot = Updater(token)

    logging.info('Bot is running')
    # Добавить обработчик
    dp = bot.dispatcher
    # Обработчик комманд
    dp.add_handler(CommandHandler("start", greeting))
    # Обработчик сообщений
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # начать проверку сообщений
    bot.start_polling()
    # работать до момента остановки
    bot.idle()


main()