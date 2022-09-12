import os
import logging
from aiogram import Bot, Dispatcher, executor, types
# from config import API_TOKEN


# Configure logging
logging.basicConfig(level=logging.INFO, filename='logfile.log')

API_TOKEN = os.getenv('TOKEN')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# в диспетчер передаётся бот

dict_name = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д':'d', 'е':'e', 'ё':'e', 'ж':'zh',\
     'з':'z', 'и':'i', 'й':'i', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'kh', 'ц':'ts', 'ч':'ch', 'ш':'sh', 'щ':'shch', 'ъ':'ie', 'ы':'y', 'ь':'',\
     'э':'e', 'ю':'iu', 'я':'ia'}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    text = f"Привет, {user_name}! 🌝\nЯ бот, который переведёт твоё ФИО на латиницу.".format(message)
    text_2 = "Напиши своё ФИО:\nФамилия Имя Отчество"
    user_id = message.from_user.id
    logging.info(f"{user_name=} {user_id=} send message: {message.text}")
    await message.answer(text)
    await message.answer(text_2)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    text = "Напиши свою фамилию, имя и отчество на латинице без знаков препинания через пробел: Фамилия Имя Отчество\n\nНапример: Иван Иванович Иванов\n\nPS: чтобы бот работал корректно - проверь свою орфографию!"
    user_id = message.from_user.id
    logging.info(f"{user_name=} {user_id=} send message: {message.text}")
    await message.answer(text)

@dp.message_handler()
async def get_lastname(message: types.Message):
    name = message.text
    logging.info(f"send message: {name}")
    split_name = name.split()
    if len(split_name) == 3:
        new_name = [j for i in name.lower().split() for j in i if j not in dict_name.keys()]
        if len(new_name) == 0:
            output_name = transate_name(name)
            await message.answer('Отлично❤️')
            logging.info(f"get {name} -> send {output_name}")
            await message.answer(output_name)
        else:
            await message.answer('Неверно! Введи, пожалуйста, буквы на кириллице.')
    else:
        await message.answer('Неверно! Попробуй ввести ещё раз.')
    # else:
    #     bot.send_message(message.from_user.id, 'Напиши фио')
# aiogram - асинхронная библиотека
# все запросы обрабатываются параллельно
# async - указываем, что наша функция должна быть асинхронной

def transate_name(message: str):
    name = message
    t_name = []
    split_name = name.lower().split()
    for i in split_name:
        for j in i:
            t_name.append(dict_name[j])
        t_name.append(' ')
    t_name.pop()
    return ''.join(t_name).title()




# @dp.message_handler()
# async def echo(message: types.Message):
#     user_name = message.from_user.first_name
#     text = message.text
#     user_id = message.from_user.id
#     logging.info(f"{user_name=} {user_id=} send message: {text}")
#     await message.answer(text)
# асинхронные функции позволяют несколько раз отправлять await

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)