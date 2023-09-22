from Dispatcher import dp

from states.database import insert_data
from keyboards.keyboards import contact_keyboard
from states.states import UserState

from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext


@dp.callback_query(lambda callback_query: callback_query.data == 'confirm')
async def confirm(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    take = data['phone']
    if str(take)[0] == '+':
        phone = str(take).split()[0].split('+')[1]
    else:
        phone = take
    user_data = dict(
        phone=phone,
        first_name=data['first_name'],
        last_name=data['last_name'],
        address=data['address']
    )
    insert_data(user_data)
    await state.storage.close()
    await state.clear()
    await callback_query.message.answer('Successfully registered!')
    await callback_query.message.delete()


@dp.callback_query(lambda callback_query: callback_query.data == 'cancel')
async def cancel(callback_query: CallbackQuery, state: FSMContext):
    await state.storage.close()
    await state.clear()
    await callback_query.message.answer('Canceled. Please try again')
    await callback_query.message.delete()
    first_name = callback_query.message.from_user.first_name
    reply_markup = contact_keyboard()
    await callback_query.message.answer(
        f"Hello {first_name}! Please share your contact.",
        reply_markup=reply_markup
    )
    await state.set_state(UserState.phone)


@dp.callback_query(lambda callback_query: callback_query.data == 'feels')
async def temp(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    weather = data['weather']
    await callback_query.message.answer(f"🌡 Feels like: {str(weather['main']['feels_like'])}")


@dp.callback_query(lambda callback_query: callback_query.data == 'pressure')
async def pressure(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    pressure = data['weather']
    await callback_query.message.answer(f"🌬 Pressure: {str(pressure['main']['pressure'])}")


@dp.callback_query(lambda callback_query: callback_query.data == 'humidity')
async def humidity(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    humidity = data['weather']
    await callback_query.message.answer(f"🌫 Humidity: {str(humidity['main']['humidity'])}")


@dp.callback_query(lambda callback_query: callback_query.data == 'all informations')
async def all(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    all = data['weather']
    await callback_query.message.answer((f"🌡 Temperature: {str(all['main']['temp']) + '°C'}\n"
                                         f"🌡 Feels like: {str(all['main']['feels_like']) + '°C'}"
                                         f"\n🌬 Pressure: {str(all['main']['pressure'])}"
                                         f"\n🌫 Humidity: {str(all['main']['humidity'])}"))
