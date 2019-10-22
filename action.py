from telebot import TeleBot, types
from datetime import datetime
from lists import rand_win, rand_lose, rand_draw
from db_operations import db_update_win, db_update_lose, db_update_draw, db_read


bot = TeleBot("980088298:AAGygISzDgEle6OvSuHdJ2Nv0vwLhK_CxVE")


def log(message, answer, *args):
    print("\n--------------------")
    print(datetime.now().strftime('%d.%m.%Y_%H:%M'))
    print("Сообщение от {0} {1} \nusername: {2}  (id = {3}) \nТекст: {4}".format(
        message.from_user.first_name,
        message.from_user.last_name,
        message.from_user.username,
        str(message.from_user.id),
        message.text,))
    print(f"Ответ: {answer}.", *args)


def log_reset(call):
    print("\n--------------------")
    print(datetime.now().strftime('%d.%m.%Y_%H:%M'))
    print("Сообщение от {0} {1} \nusername: {2}  (id = {3}) \nБыл сделан сброс".format(
        call.from_user.first_name,
        call.from_user.last_name,
        call.from_user.username,
        str(call.from_user.id),))


def start_menu(message):
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row("👊🏻", "✌🏻", "✋🏻")
    user_markup.row("Посмотреть счет 🧮")
    answer = "Ну что, сыграем 🎮⁉️"
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    log(message, answer)


def win(message, step_bot):
    db_update_win(message)
    answer1 = step_bot
    answer2 = rand_win()
    bot.send_message(message.from_user.id, answer1)
    bot.send_message(message.from_user.id, answer2)
    log(message, answer1, answer2)


def lose(message, step_bot):
    db_update_lose(message)
    answer1 = step_bot
    answer2 = rand_lose()
    bot.send_message(message.from_user.id, answer1)
    bot.send_message(message.from_user.id, answer2)
    log(message, answer1, answer2)


def draw(message, step_bot):
    db_update_draw(message)
    answer1 = step_bot
    answer2 = rand_draw()
    bot.send_message(message.from_user.id, answer1)
    bot.send_message(message.from_user.id, answer2)
    log(message, answer1, answer2)


def see_score(message):
    answer = f"Результаты игры:\n👍 Побед: {db_read(message.from_user.id)[0]} 🏆\n" \
             f"👎 Поражений: {db_read(message.from_user.id)[1]} 🚽\n🤝 Ничьи: {db_read(message.from_user.id)[2]} 🕊️"
    bot.send_message(message.from_user.id, answer)
    log(message, answer)
