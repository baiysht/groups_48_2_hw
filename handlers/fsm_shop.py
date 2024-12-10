# fsm_reg.py
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cancel_markup, start_markup
from aiogram.types import ReplyKeyboardRemove

class FSMShop(StatesGroup):
    Modelname = State()
    Size = State()
    Category = State()
    Price = State()
    Photo = State()
    Submit = State()


async def start_fsm_shop(message: types.Message):
    await message.answer('Введите название модели:', reply_markup=cancel_markup)
    await FSMShop.Modelname.set()

async def load_modelname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['modelname'] = message.text

    await FSMShop.next()
    await message.answer('Укажите свой размер:', reply_markup=cancel_markup)


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSMShop.next()
    await message.answer('Укажите категорию товара:', reply_markup=cancel_markup)


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSMShop.next()
    await message.answer('Укажите цену товара:', reply_markup=cancel_markup)


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await FSMShop.next()
    await message.answer('Отправьте фотку товара:', reply_markup=cancel_markup)


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMShop.next()
    await message.answer(f'Верные ли данные?')
    await message.answer_photo(photo=data['photo'],
                               caption=f'ФИО - {data["fullname"]}\n'
                             f'Возраст - {data["age"]}\n'
                             f'Пол - {data["gender"]}\n'
                             f'Почта - {data["email"]}\n')


async def load_submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        async with state.proxy() as data:
            # Запись в базу
            await message.answer('Ваши данные в базе!')
            await state.finish()

    elif message.text == 'Нет':
        await message.answer('Хорошо, отменено!')
        await state.finish()

    else:
        await message.answer('Введите Да или Нет!')

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=start_markup)


def register_fsmshop_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True), state='*')

    dp.register_message_handler(start_fsm_shop, commands=['buy'])
    dp.register_message_handler(load_modelname, state=FSMShop.Modelname)
    dp.register_message_handler(load_size, state=FSMShop.Size)
    dp.register_message_handler(load_category, state=FSMShop.Category)
    dp.register_message_handler(load_price, state=FSMShop.Price)
    dp.register_message_handler(load_photo, state=FSMShop.Photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=FSMShop.Submit)