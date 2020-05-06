import telebot
import random
import sys

def generate_markup(buttons):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    list_items = []
    for item in buttons:
        list_items.append(item)
    random.shuffle(list_items)
    for item in list_items:
        markup.add(item)
    return markup


def generate_inline_markup(buttons):
    for item in buttons:
        print(sys.getsizeof(item))
        print(sys.getsizeof(buttons[item]))
    keyboard = [telebot.types.InlineKeyboardButton(item, callback_data=buttons[item]) for item in buttons]
    random.shuffle(keyboard)
    markup = telebot.types.InlineKeyboardMarkup()
    for item in keyboard:
        markup.add(item)
    return markup


