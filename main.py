# # import asyncio
# # import os
# #
# # from aiogram import Bot, Dispatcher
# # from aiogram.types import Message
# # from aiogram.filters import CommandStart
# #
# # from dotenv import load_dotenv
# #
# # load_dotenv()
# #
# # TOKEN =os.getenv('BOT_TOKEN')
# # APIKEY=os.getenv('APIKEY')
# #
# # dp = Dispatcher()
# #
# # @dp.message(CommandStart())
# # async def startup(message: Message):
# #     first_name=message.from_user.first_name
# #     await message.answer(f"Hello {first_name}!\nWelcome to telegram bot")
# #
# # @dp.message(lambda msg: msg.text == '/help')
# # async def help_function(message: Message):
# #     await message.answer('Welcome to our bot!')
# #
# # @dp.message(lambda msg: msg.text=='/stop')
# # async def stop_it(message:Message):
# #     await message.answer('Ok!\nThe bot was stopped')
# #
# # async def main():
# #     bot = Bot(TOKEN)
# #     await dp.start_polling(bot)
# #
# # if __name__ == '__main__':
# #     asyncio.run(main())
# ###############################################################################
#
# import os
# import asyncio
#
# from aiogram import Bot, Dispatcher
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
# from aiogram.filters import CommandStart
#
# from dotenv import load_dotenv
#
# from code import get_temperature
#
# load_dotenv()
#
# TOKEN = os.getenv('TOKEN')
#
# dp = Dispatcher()
# DATA = None
#
#
# @dp.message(CommandStart())
# async def startup(message: Message):
#     first_name = message.from_user.first_name
#     await message.answer(f"Hello {first_name}!")
#
#
# @dp.message(lambda msg: msg.text == '/weather')
# async def weather(message: Message):
#     await message.answer("Please enter your city name")
#
#
# @dp.message(lambda msg: msg.text in ['Maximum temperature', 'Minimum temperature', 'Pressure', 'Humidity','All informations'])
# async def click(message: Message):
#     dtb = None
#
#     match message.text:
#         case 'Maximum temperature':
#             dtb = DATA['main']['temp_max']
#         case 'Minimum temperature':
#             dtb = DATA['main']['temp_min']
#         case 'Pressure':
#             dtb = DATA['main']['pressure']
#         case 'Humidity':
#             dtb = DATA['main']['humidity']
#         case 'All informations':
#             dtb=f"Temperature: {DATA['main']['temp_max']}\nMinimum temperature: {DATA['main']['temp_min']}\nPressure: {DATA['main']['pressure']}\nHumidity: {DATA['main']['humidity']}\nSpeed: {DATA['wind']['speed']}"
#
#     await message.answer(str(dtb))
#
# @dp.message()
# async def show_weather(message: Message):
#     city = message.text
#     response = get_temperature(city)
#     if response['cod'] != "404":
#         text = f'Temperature: {response["main"]["temp"]}'
#         global DATA
#         DATA = response
#         max_temp_btn = KeyboardButton(text='Maximum temperature')
#         min_temp_btn = KeyboardButton(text='Minimum temperature')
#         pressure_btn = KeyboardButton(text='Pressure')
#         humidity_btn = KeyboardButton(text='Humidity')
#         all_informs=KeyboardButton(text='All informations')
#         reply_markup = ReplyKeyboardMarkup(keyboard=[[max_temp_btn], [min_temp_btn], [pressure_btn], [humidity_btn,all_informs]], resize_keyboard=True)
#         await message.answer(text, reply_markup=reply_markup)
#     else:
#         text = 'City not found, please try again!'
#         await message.answer(text)
#
#
# @dp.message(lambda msg: msg.text == '/help')
# async def help_function(message: Message):
#     await message.answer('Welcome to our bot!')
#
#
# async def main():
#     bot = Bot(TOKEN)
#     await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
#########################################################################

# NEW BOT: THROUGH LOCATION WEATHER BOT

# import os
# import asyncio
#
# from aiogram import Bot, Dispatcher
# from aiogram.types import (
#     ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Message,CallbackQuery)
# from aiogram.filters import CommandStart
# from dotenv import load_dotenv
#
# from code import get_weather_data
#
# load_dotenv()
#
# dp = Dispatcher()
# BOT = os.getenv('P15BOT')
#
#
# @dp.message(CommandStart())
# async def start(message: Message):
#     location_btn = KeyboardButton(text='Share location', request_location=True)
#     reply_markup = ReplyKeyboardMarkup(keyboard=[[location_btn]], resize_keyboard=True,one_time_keyboard=True)
#     first_name=message.from_user.first_name
#     await message.answer(f"Hello {first_name}!", reply_markup=reply_markup)
#
#
# @dp.message(lambda msg: msg.text == '/help')
# async def helps(message: Message):
#     await message.answer('This is very useful bot for you')
#
#
# @dp.message(lambda msg: msg.location is not None)
# async def get_location(message: Message):
#     lon = str(message.location).split()[0].split('=')[1]
#     lat = str(message.location).split()[1].split('=')[1]
#     response = get_weather_data(lon, lat)
#     if response['cod'] != 404:
#         global DATA
#         DATA = response
#         temp = str(round(response['main']['temp'], 1)) + 'C'
#
#     else:
#         temp = 'City not found'
#     city_btn = InlineKeyboardButton(text='City', callback_data='Name')
#     pressure_btn = InlineKeyboardButton(text='Pressure', callback_data='Pressure')
#     humidity_btn = InlineKeyboardButton(text='Humidity', callback_data='Humidity')
#     all_informs=InlineKeyboardButton(text='All informations',callback_data='All informations')
#     reply_markup = InlineKeyboardMarkup(inline_keyboard=[[city_btn, pressure_btn],[humidity_btn, all_informs]])
#     await message.answer(temp, reply_markup=reply_markup)
#
# @dp.callback_query(lambda callback_query: callback_query.data=='Name')
# async def get_name(callback_query:CallbackQuery):
#     name=DATA['name']
#     await callback_query.message.answer(name)
#
# @dp.callback_query(lambda callback_query: callback_query.data=='Pressure')
# async def get_pressure(callback_query: CallbackQuery):
#     name=str(DATA['main']['pressure'])
#     await callback_query.message.answer(name)
#
# @dp.callback_query(lambda callback_query: callback_query.data=='Humidity')
# async def get_humidity(callback_query: CallbackQuery):
#     name=str(DATA['main']['humidity'])
#     await callback_query.message.answer(name)
#
# @dp.callback_query(lambda callback_query: callback_query.data=='All informations')
# async def get_all(callback_query: CallbackQuery):
#     name=f"City: {DATA['name']}\nPressure: {str(DATA['main']['pressure'])}\nHumidity: {str(DATA['main']['humidity'])}"
#     await callback_query.message.answer(name)
#
# async def main():
#     bot = Bot(BOT)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
##############################################################################################


# import asyncio
# import os
#
#
# from aiogram import Bot,Dispatcher
# from aiogram.fsm import state
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import (
#     Message, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, ContentType,
#     InlineKeyboardMarkup, ReplyKeyboardRemove)
#
# from dotenv import load_dotenv
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
#
# from code import get_address_using_location
# from states.database import insert_data, is_exist
# from states.states import UserState
#
# load_dotenv()
#
# dp=Dispatcher(storage=MemoryStorage())
#
# from code import get_weather_data
#
# BOT = os.getenv('P15BOT')
#
#
# def weather():
#     @dp.message()
#     async def start(message: Message):
#         first_name=message.from_user.first_name
#         location_btn = KeyboardButton(text='Share location', request_location=True)
#         reply_markup = ReplyKeyboardMarkup(keyboard=[[location_btn]], resize_keyboard=True,one_time_keyboard=True)
#         await message.answer(f"{first_name} Welcome to weather bot !",reply_markup=reply_markup)
#         await message.delete()
#
#     @dp.message(lambda msg: msg.location is not None)
#     async def get_location(message: Message):
#         lon = str(message.location).split()[0].split('=')[1]
#         lat = str(message.location).split()[1].split('=')[1]
#         response = get_weather_data(lon, lat)
#         if response['cod'] != 404:
#             global DATA
#             DATA = response
#             temp = str(round(response['main']['temp'], 1)) + 'C'
#
#         else:
#             temp = 'City not found'
#         city_btn = InlineKeyboardButton(text='City', callback_data='Name')
#         pressure_btn = InlineKeyboardButton(text='Pressure', callback_data='Pressure')
#         humidity_btn = InlineKeyboardButton(text='Humidity', callback_data='Humidity')
#         all_informs=InlineKeyboardButton(text='All informations',callback_data='All informations')
#         reply_markup = InlineKeyboardMarkup(inline_keyboard=[[city_btn, pressure_btn],[humidity_btn, all_informs]])
#         await message.answer(temp, reply_markup=reply_markup)
#
#     @dp.callback_query(lambda callback_query: callback_query.data=='Name')
#     async def get_name(callback_query:CallbackQuery):
#         name=DATA['name']
#         await callback_query.message.answer(name)
#
#     @dp.callback_query(lambda callback_query: callback_query.data=='Pressure')
#     async def get_pressure(callback_query: CallbackQuery):
#         name=str(DATA['main']['pressure'])
#         await callback_query.message.answer(name)
#
#     @dp.callback_query(lambda callback_query: callback_query.data=='Humidity')
#     async def get_humidity(callback_query: CallbackQuery):
#         name=str(DATA['main']['humidity'])
#         await callback_query.message.answer(name)
#
#     @dp.callback_query(lambda callback_query: callback_query.data=='All informations')
#     async def get_all(callback_query: CallbackQuery):
#         name=f"City: {DATA['name']}\nPressure: {str(DATA['main']['pressure'])}\nHumidity: {str(DATA['main']['humidity'])}"
#         await callback_query.message.answer(name)


# @dp.message(lambda msg: msg.text=='/login')
# async def login(message:Message):
#     await message.answer('Please enter your phone number: ')
#     await message.delete()
#
#
# @dp.message(lambda msg: msg.text is not None)
# async def for_weather(message: Message, state: FSMContext):
#     contact=message.text
#     await state.update_data({
#         'phone': contact
#     })
#     await message.answer('Enter your first name: ')
#     await state.set_state(UserState.first_name)
#
# @dp.message(UserState.first_name)
# async def for_weather_phone(message: Message, state: FSMContext):
#     await state.update_data({
#         'first_name': message.text
#     })
#     data=await state.get_data()
#     name=data['first_name']
#     number=data['phone']
#     if is_exist(name, number):
#         weather()
#     await state.storage.close()
#     await state.clear()
#     await message.delete()


import os
import asyncio

from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from dotenv import load_dotenv
from states.database import is_exist
from code import get_temperature, get_address_location
from keyboards.keyboards import contact_keyboard, location_keyboard, client_choice, weather_informations
from states.states import UserState
from Dispatcher import dp
from commands.commands import start, help, login
from callback_handler import callbackhandlers

load_dotenv()


@dp.message(CommandStart())
async def startup(message: Message, state: FSMContext):
    first_name = message.from_user.first_name
    reply_markup = contact_keyboard()
    await message.answer(
        f"Hello {first_name}!",
        reply_markup=reply_markup
    )
    await message.delete()
    await state.set_state(UserState.phone)


@dp.message(UserState.phone)
async def phone(message: Message, state: FSMContext):
    contact = message.contact
    await state.update_data({
        'phone': contact.phone_number
    })
    await message.answer('Enter your first name', reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserState.first_name)


@dp.message(UserState.first_name)
async def first_name(message: Message, state: FSMContext):
    await state.update_data({
        'first_name': message.text
    })
    await message.answer('Enter your last name')
    await state.set_state(UserState.last_name)


@dp.message(UserState.last_name)
async def last_name(message: Message, state: FSMContext):
    await state.update_data({
        'last_name': message.text
    })
    reply_markup = location_keyboard()
    await message.answer('Share your location', reply_markup=reply_markup)
    await state.set_state(UserState.address)


@dp.message(UserState.address)
async def address(message: Message, state: FSMContext):
    location = message.location
    lon = location.longitude
    lat = location.latitude
    city = get_address_location(lat, lon)
    await state.update_data({
        'address': city
    })
    data = await state.get_data()
    phone = data['phone']
    first_name = data['first_name']
    last_name = data['last_name']
    address = data['address']
    msg = f'''
    📞 Phone number: {phone}
    🧍‍♂️First name: {first_name}
    🧍‍♂️Last name: {last_name}
    🌍Address: {address}
        '''
    await message.answer('Confirm or Cancel', reply_markup=ReplyKeyboardRemove())
    reply_markup = client_choice()
    await message.answer(msg, reply_markup=reply_markup)


@dp.message(lambda msg: msg.location is not None)
async def get_weather(message: Message, state: FSMContext):
    location = message.location
    lon = location.longitude
    lat = location.latitude
    temp = get_temperature(lat, lon)
    await state.update_data({
        'weather': temp
    })
    reply_markup = weather_informations()
    await message.answer(f"🌡 Temperature: {str(round(temp['main']['temp'], 1)) + '°C'}", reply_markup=reply_markup)


@dp.message(lambda msg: msg.contact is not None)
async def log_to_bot(message: Message, state: FSMContext):
    contact = message.contact
    await state.update_data({
        'logphone': contact.phone_number
    })
    await message.answer('Enter your last name', reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserState.last)


@dp.message(UserState.last)
async def checks(message: Message, state: FSMContext):
    first = message.text
    await state.update_data({
        'last': first
    })
    data = await state.get_data()
    num = data['logphone']
    if str(num)[0] == '+':
        phoness = str(num).split()[0].split('+')[1]
    else:
        phoness = num
    name = data['last']
    if is_exist(name, phoness):
        await message.answer('You logged successfully!', reply_markup=ReplyKeyboardRemove())
        reply_markup = location_keyboard()
        await message.answer('Share your location to know current weather: ', reply_markup=reply_markup)
        await message.delete()
    else:
        await message.answer('Wrong data!', reply_markup=ReplyKeyboardRemove())
        reply_markup = contact_keyboard()
        await message.answer('Try again!', reply_markup=reply_markup)
        await state.set_state(UserState.last)
        await state.storage.close()
        await state.clear()


async def main():
    token = os.getenv('USERS')
    bot = Bot(token)
    await bot.set_my_commands(commands=[start, help, login])
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
