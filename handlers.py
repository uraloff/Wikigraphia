from aiogram.types import Message, CallbackQuery
import keyboards as kb
from aiogram import Router, F
import photos
import countries


router = Router()


@router.message(F.text == '/start')
async def start(message: Message):
    username = message.from_user.first_name
    await message.answer(f'Здарова <strong>{username}</strong>! Мы рады приветствовать тебя в нашем телеграм-боте. Здесь ты сможешь найти полезную информацию об определённой стране', parse_mode='HTML', reply_markup=kb.main_kb)


@router.message(F.text.in_({'Помощь ❗️', '/help'}))
async def proccess_if_help(message: Message):
    await message.answer("Этот бот предназначен для предоставления информации об определённой стране. Введи название страны, а я предоставлю тебе информацию об этой стране\n- чтобы бот работал корректно постарайся написать название стран без ошибок\n\n<strong>Пример:</strong>\n❌ Узб, UZB, O'zbekiston, Uzbekistan, 🇺🇿;\n✅ Узбекистан, узбекистан.\n- все информации берутся из Википедии\n- если заметил(-а) ошибку, просим проинформировать об этом админу в описании бота\n- если информация неактуальна, а в Википедии ещё не изменено, просим об этом тоже проинформировать\n\n<strong>Важно!</strong>\nДля этого нам необходимо доказательства, при этом мы не принимаем новостей из СМИ, мы принимаем только официальных доказательств (например, из официальных государственных сайтах)", parse_mode='HTML')
    

@router.message(F.text == 'Главное меню ✅')
async def main_menu_process(message: Message):
    await message.answer('Что ищем?', reply_markup=kb.main_menu)
#    @router.message(F.text == 'Украина')
#    async def check_countries(message: Message):
#        if message.text == 'Украина':
#            await message.answer_photo(photo=photos.ukr_photo.name, 
#                                       caption=f'🏳️ Страна: {countries.ukr.name}\n⭐️ Столица: {countries.ukr.capital}\n📅 Дата независимости: {countries.ukr.indday}\n🔠 Официальный язык: {countries.ukr.lang}\n🎶 Гимн: {countries.ukr.anthem}\n⛳️ Территория: {countries.ukr.area}\n👑 Форма правления: {countries.ukr.gov}\n👥 Соседи: {countries.ukr.neighbors}\n📞 Телефонный код: {countries.ukr.tel_code}\n☦️ Религия: {countries.ukr.religion}\n👨‍👩‍👧‍👦 Население: {countries.ukr.population}\n💰 Валюта: {countries.ukr.currency}\n🕐 Часовой пояс: {countries.ukr.time_zone}\n🌐 Интернет-домен: {countries.ukr.net_domain}\n📝 Описание: {countries.ukr.about}')



@router.callback_query(F.data == 'info')
async def cb_info(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Введи страну:', reply_markup=kb.search_menu_1)
    await callback.message.delete()

@router.callback_query(F.data == 'symbol')
async def cb_symbol(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Какую из них?', reply_markup=kb.symbols_menu)
    await callback.message.delete()
    

@router.callback_query(F.data == 'back_1')
async def cb_back_1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Что ищем?', reply_markup=kb.main_menu)
    await callback.message.delete()


@router.callback_query(F.data == 'flag')
async def cb_flag(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Введи страну:', reply_markup=kb.search_menu_3)
    await callback.message.delete()
@router.callback_query(F.data == 'emblem')
async def cb_emblem(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Введи страну:', reply_markup=kb.search_menu_3)
    await callback.message.delete()
@router.callback_query(F.data == 'anthem')
async def cb_anthem(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Введи страну:', reply_markup=kb.search_menu_3)
    await callback.message.delete()
@router.callback_query(F.data == 'back_2')
async def cb_back_2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Что ищем?', reply_markup=kb.main_menu)
    await callback.message.delete()


@router.callback_query(F.data == 'back_3')
async def cb_back_3(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Какую из них?', reply_markup=kb.symbols_menu)
    await callback.message.delete()

        
@router.callback_query(F.data == 'main_menu_ikb')
async def cb_main_menu_ikb(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Что ищем?', reply_markup=kb.main_menu)
    await callback.message.delete()
@router.callback_query(F.data == 'help_ikb')
async def cb_help_ikb(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Этот бот предназначен для предоставления информации об определённой стране. Введи название страны, а я предоставлю тебе информацию об этой стране\n- чтобы бот работал корректно постарайся написать название стран без ошибок\n\n<strong>Пример:</strong>\n❌ Узб, UZB, O'zbekiston, Uzbekistan, 🇺🇿;\n✅ Узбекистан, узбекистан.\n- все информации берутся из Википедии\n- если заметил(-а) ошибку, просим проинформировать об этом админу в описании бота\n- если информация неактуальна, а в Википедии ещё не изменено, просим об этом тоже проинформировать\n\n<strong>Важно!</strong>\nДля этого нам необходимо доказательства, при этом мы не принимаем новостей из СМИ, мы принимаем только официальных доказательств (например, из официальных государственных сайтах)", parse_mode='HTML')
    await callback.message.delete()


@router.message()
async def else_situation(message: Message):
#    await message.reply('Вроде такой страны не существует.\nНажмите на "Главное меню ✅", чтобы перейти на главное меню или нажмите на "Помощь ❗️", чтобы посмотреть на правила', reply_markup=kb.main_ikb)
    await message.answer_photo(photo=photos.uzb_photo.name)

