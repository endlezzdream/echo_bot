from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard1():
    keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('отправь картинку в стиле yabujin')
    button2 = KeyboardButton('>>')
    keyboard1.add(button1, button2)
    return keyboard1


def get_keyboard2():
    keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button4 = KeyboardButton('как выглядят низкие абстракты с мехом?')
    button3 = KeyboardButton('<<')
    keyboard2.add(button3, button4)
    return keyboard2
