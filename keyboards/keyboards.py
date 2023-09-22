from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


def contact_keyboard():
    contact = KeyboardButton(text="☎️ Share contact", request_contact=True)
    reply_markup = ReplyKeyboardMarkup(keyboard=[[contact]], resize_keyboard=True, one_time_keyboard=True)

    return reply_markup


def languages():
    uzbek = KeyboardButton(text='Uzbek')
    rus = KeyboardButton(text='Russia')
    eng = KeyboardButton(text='English')
    reply_markup = ReplyKeyboardMarkup(keyboard=[[uzbek], [rus], [eng]], resize_keyboard=True, one_time_keyboard=True)

    return reply_markup


def location_keyboard():
    location_btn = KeyboardButton(text='📍 Share your location', request_location=True)
    reply_markup = ReplyKeyboardMarkup(keyboard=[[location_btn]], resize_keyboard=True, one_time_keyboard=True)

    return reply_markup


def client_choice():
    confirm_btn = InlineKeyboardButton(text='Confirm', callback_data='confirm')
    cancel_btn = InlineKeyboardButton(text='Cancel', callback_data='cancel')
    reply_markup = InlineKeyboardMarkup(inline_keyboard=[[confirm_btn, cancel_btn]])

    return reply_markup


def weather_informations():
    city_btn = InlineKeyboardButton(text='🌡 Feels like', callback_data='feels')
    pressure_btn = InlineKeyboardButton(text='🌬 Pressure', callback_data='pressure')
    humidity_btn = InlineKeyboardButton(text='🌡 Humidity', callback_data='humidity')
    all_inform = InlineKeyboardButton(text='All informations', callback_data='all informations')
    reply_markup = InlineKeyboardMarkup(inline_keyboard=[[city_btn, pressure_btn], [humidity_btn, all_inform]])

    return reply_markup


def lang_key():
    eng = InlineKeyboardButton(text='English', callback_data='English')
    rus = InlineKeyboardButton(text='Русский', callback_data='Русский')
    reply = InlineKeyboardMarkup(inline_keyboard=[[eng, rus]])

    return reply
