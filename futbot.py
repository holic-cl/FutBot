#!/bin/python
# -*- coding: utf-8 -*-
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from settings import BOT_TOKEN
import commands
import logging

logger = logging.getLogger(__name__)


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    start_handler = CommandHandler('start', commands.start)
    dispatcher.add_handler(start_handler)
    statistics_handler = CommandHandler('estadisticas', commands.get_statistics)
    dispatcher.add_handler(statistics_handler)

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    # log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
