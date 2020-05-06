import config
import utils
import telebot

use_inline_markup = True

bot = telebot.TeleBot(config.token)


@bot.message_handler(func=lambda query: True, commands=['enter'])
def game(message):
    if use_inline_markup:
        markup = utils.generate_inline_markup(config.buttons_for_inline)
    else:
        markup = utils.generate_markup(config.buttons)
    bot.send_message(message.chat.id, config.pre_button_reaction, reply_markup=markup)


@bot.message_handler(func=lambda mes: mes in config.buttons.keys(), content_types=['text'])
def check_answer(message):
    hide_keyboard = telebot.types.ReplyKeyboardRemove()
    if message.text in config.buttons:
        bot.send_message(message.chat.id, config.buttons[message.text], reply_markup=hide_keyboard)
    else:
        bot.send_message(message.chat.id, config.confusion, reply_markup=hide_keyboard)
        game(message)


@bot.callback_query_handler(func=lambda call: call.data == '0' or call.data == '1')
def callback_inline(call):
    if call.message:
        bot.send_message(call.message.chat.id, 'Тогда пойдем выйдем')
    else:
        print('jej 404')


@bot.callback_query_handler(func=lambda call: call.data == '2')
def callback_inline(call):
    if call.message:
        bot.send_message(call.message.chat.id, 'ААРАРРАРАЩЦАЩЦООЙЦ!!! Выйди вон отсюда...')
    else:
        print('jej 404')


@bot.message_handler(content_types=["text"])
def repeat_mes(message):
    bot.send_message(message.chat.id, config.default_message)


if __name__ == '__main__':
    bot.infinity_polling()