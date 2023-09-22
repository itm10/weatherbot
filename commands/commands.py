from aiogram.types.bot_command import BotCommand
from aiogram.filters.command import Command
from aiogram.types import Message

from Dispatcher import dp
from keyboards.keyboards import location_keyboard, contact_keyboard

start = BotCommand(command='start', description='Start bot')
help = BotCommand(command='help', description='Help command')
weather = BotCommand(command='weather', description='Weather in your current location')
login = BotCommand(command='login', description='Log into a bot')


@dp.message(Command(help))
async def help_function(message: Message):
    await message.answer('You can control me by sending these commands:\n\n'
                         '/start - start a bot\n'
                         '/help - get a guide\n'
                         '/login - log into a bot')


@dp.message(Command(weather))
async def weather_command(message: Message):
    reply_markup = location_keyboard()
    await message.answer("Share your location", reply_markup=reply_markup)


@dp.message(Command(login))
async def login_command(message: Message):
    reply_markup = contact_keyboard()
    await message.answer('Share your exists phone number: ', reply_markup=reply_markup)
