from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_inline1():
    keyboard_inline1 = InlineKeyboardMarkup(row_width=1)
    but_inline1 = InlineKeyboardButton('посмотреть', url='https://genius.com/artists/Yabujin')
    keyboard_inline1.add(but_inline1)
    return keyboard_inline1


def get_keyboard_inline2():
    keyboard_inline2 = InlineKeyboardMarkup(row_width=1)
    but_inline2 = InlineKeyboardButton('посмотреть', url='https://www.farfetch.com/shopping/women/rick-owens-drkshdw-abstract-low-faux-fur-sneakers-item-19049566.aspx')
    keyboard_inline2.add(but_inline2)
    return keyboard_inline2
