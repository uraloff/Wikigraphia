from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Главное меню ✅'),
    KeyboardButton(text='Помощь ❗️')]
],
                              resize_keyboard=True)


main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📋 Краткое инфо о стране', callback_data='info')],
    [InlineKeyboardButton(text='⚜️ Госсимволы страны', callback_data='symbol')]
])


search_menu_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад ↩️', callback_data='back_1')]
])

symbols_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Флаг 🏳', callback_data='flag')],
    [InlineKeyboardButton(text='Герб ⭐', callback_data='emblem')],
    [InlineKeyboardButton(text='Гимн 🎶', callback_data='anthem')],
    [InlineKeyboardButton(text='Назад ↩️', callback_data='back_2')]
])

search_menu_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад ↩️', callback_data='back_3')]
])

main_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Главное меню ✅', callback_data='main_menu_ikb')],
    [InlineKeyboardButton(text='Помощь ❗️', callback_data='help_ikb')]
])