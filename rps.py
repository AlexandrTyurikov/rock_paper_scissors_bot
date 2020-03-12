from telebot import TeleBot, types
from db_operations import db_add_user, db_date_last_visit, db_all_id, db_reset_results
from action import start_menu, win, lose, draw, log, log_reset, see_score
from lists import rand_rps, rand_emoji


bot = TeleBot("Ваш API-токен бота")

print(bot.get_me())


@bot.message_handler(commands=['start'])
def handler_start(message: types.Message):
    try:
        if message.from_user.id not in db_all_id():
            start_menu(message)
            db_add_user(message)
        else:
            start_menu(message)
    except Exception as e:
        print("Exception (find):", e)
        pass


@bot.message_handler(commands=['reset'])
def handler_reset(message: types.Message):
    try:
        reset_keyboard = types.InlineKeyboardMarkup()
        reset_no = types.InlineKeyboardButton(text='НЕТ, НЕ НАДО', callback_data='no')
        reset_yes = types.InlineKeyboardButton(text='ДА, СБРОСИТЬ', callback_data='yes')
        reset_keyboard.add(reset_no, reset_yes)
        answer = "Уверен что хочешь сбросить счет?"
        bot.send_message(message.chat.id, answer, reply_markup=reset_keyboard)
        log(message, answer)
    except Exception as e:
        print("Exception (find):", e)
        pass


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call: types.CallbackQuery):
    try:
        if call.data == 'yes':
            reset_yes = types.InlineKeyboardMarkup()
            reset_no2 = types.InlineKeyboardButton(text='НЕТ, ПЕРЕДУМАЛ', callback_data='no2')
            reset_yes2 = types.InlineKeyboardButton(text='ДА, НА 100% УВЕРЕН', callback_data='yes2')
            reset_yes.add(reset_no2, reset_yes2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Точно уверен? Все достижения будут сброшены!', reply_markup=reset_yes)
        elif call.data == 'no' or call.data == 'no2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Тогда продолжем играть")
        elif call.data == 'yes2':
            db_reset_results(call)
            bot.answer_callback_query(callback_query_id=call.id, text='Счет сброшен', show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="Ну что ж, начнем сначало")
            log_reset(call)
    except Exception as e:
        print("Exception (find):", e)
        pass


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def handler_message(message: types.Message):
    try:
        db_date_last_visit(message)
        step_bot = rand_rps()
        if message.text == step_bot:
            draw(message, step_bot)
        elif message.text == '👊🏻' and step_bot == '✌🏻':
            win(message, step_bot)
        elif message.text == '👊🏻' and step_bot == '✋🏻':
            lose(message, step_bot)
        elif message.text == '✌🏻' and step_bot == '✋🏻':
            win(message, step_bot)
        elif message.text == '✌🏻' and step_bot == '👊🏻':
            lose(message, step_bot)
        elif message.text == '✋🏻' and step_bot == '👊🏻':
            win(message, step_bot)
        elif message.text == '✋🏻' and step_bot == '✌🏻':
            lose(message, step_bot)
        elif message.text == "Посмотреть счет 🧮":
            see_score(message)
        else:
            answer = rand_emoji()
            bot.send_message(message.from_user.id, answer)
            log(message, answer)
    except Exception as e:
        print("Exception (find):", e)
        pass


@bot.message_handler(content_types=['sticker'])
def handler_sticker(message: types.Message):
    try:
        bot.send_sticker(message.from_user.id, message.sticker.file_id)
    except Exception as e:
        print("Exception (find):", e)
        pass


bot.infinity_polling(True)
bot.polling(none_stop=True, interval=0)
