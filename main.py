from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard1, get_keyboard2
from keyboard.key_inline import get_keyboard_inline1, get_keyboard_inline2
API_TOKEN = 'API_KEY'
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='запустить бота'),
        types.BotCommand(command='/help', description='узнать с чем поможет бот')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('хай, это эхобот))', reply_markup=get_keyboard1())


@dp.message_handler(lambda message: message.text == 'отправь картинку в стиле yabujin')
async def button1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://i.redd.it/42uetw7kj3bb1.jpg', caption='$&747$&4&43', reply_markup=get_keyboard_inline1())


@dp.message_handler(lambda message: message.text == '>>')
async def button2_click(message: types.Message):
    await message.answer('тут можно посмотртеть на низкие абстракты', reply_markup=get_keyboard2())


@dp.message_handler(lambda message: message.text == 'как выглядят низкие абстракты с мехом?')
async def button4_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://www.doshaburi.com/cdn/shop/collections/dsm22fw-41_1200x1200.jpg?v=1671796688', caption='вот так', reply_markup=get_keyboard_inline2())


@dp.message_handler(lambda message: message.text == '<<')
async def button3_click(message: types.Message):
    await message.answer('тут можно edbltnm z,el;by', reply_markup=get_keyboard1())


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('я не могу помочь')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
