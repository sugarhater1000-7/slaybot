import telebot
import os
import translator


BOT_TOKEN = 'TOKEN'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Что тебе перевести?")
    bot.send_message(message.chat.id, "Отправь мне txt-файл для перевода")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, 'Это не txt-файл')


@bot.message_handler(content_types=['document'])
def receive_file(message):
    # получение файла
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = './' + message.document.file_name

    # сохранение файла, если он нужного расширения
    if src.split('.')[-1] == 'txt':
        # работа с файлом
        translation = translator.translate(downloaded_file.decode("utf-8"))

        # запись в новый файл
        new_file = open(src, 'w')
        new_file.write(translation)
        new_file.close()

        # отправка файла
        bot.send_document(message.chat.id, open(src, 'rb'))

        # удаление файла
        os.remove(src)

    else:
        bot.send_message(message.chat.id, 'Не то расширение!')


bot.infinity_polling()
