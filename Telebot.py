import telebot
from telebot import types
##############################################################################
bot = telebot.TeleBot("PASTE YOUR BOT ID HERE", parse_mode=None)
#################################################################################

#This function is responsible for the operation of the main buttons
@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Расписание")
    item2 = types.KeyboardButton("Изменить расписание")
    item3 = types.KeyboardButton("Связаться с автором")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для работы с расписанием.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

# These variables store the information that the user has assigned to each day
monday = None
tuesday = None
wednesday = None
thursday = None
friday = None
saturday = None
sunday = None


@bot.message_handler(content_types=['text'])
def core(message):

    week = ["Понедельник: \n" + str(monday) + "\n\nВторник: \n" + str(tuesday) + "\n\nСреда: \n" + str(
        wednesday) + "\n\nЧетверг: \n" + str(thursday) + "\n\nПятница: \n" + str(friday) + "\n\nСуббота: \n" + str(
        saturday) + "\n\nВоскресенье:\n" + str(sunday)]

    if message.chat.type == 'private':
        if message.text == 'Расписание':
            bot.send_message(message.chat.id, week)

        elif message.text == 'Изменить расписание':

            markup = types.InlineKeyboardMarkup(row_width=7)
            item1 = types.InlineKeyboardButton("Понедельник", callback_data='mon')
            item2 = types.InlineKeyboardButton("Вторник", callback_data='tue')
            item3 = types.InlineKeyboardButton("Среда", callback_data='wed')
            item4 = types.InlineKeyboardButton("Четверг", callback_data='thu')
            item5 = types.InlineKeyboardButton("Пятница", callback_data='fri')
            item6 = types.InlineKeyboardButton("Суббота", callback_data='sat')
            item7 = types.InlineKeyboardButton("Воскресенье", callback_data='sun')
            markup.add(item1, item2, item3, item4, item5, item6, item7)

            bot.send_message(message.chat.id, 'На какой день вы хотите назначить событие?', reply_markup=markup)
        elif message.text == 'Связаться с автором':
            bot.send_message(message.chat.id, "Telegram: \n@Courier_Britva")
        else:
            bot.send_message(message.chat.id, "Я не знаю что ответить 😢\n для начала работы введите команду '/start' ")


# this function is responsible for setting a new event for each day of the week
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'mon':
                def writer1_(message):
                    global monday
                    monday = message.text
                    bot.send_message(call.message.chat.id, 'Изменения на понедельник успешно сохранены!')


                msg = bot.send_message(call.message.chat.id, 'Укажите, какое событие сохарнить на этот день:')
                bot.register_next_step_handler(msg, writer1_)



            elif call.data == 'tue':
                def writer2_(message):
                    global tuesday
                    tuesday = message.text
                    bot.send_message(call.message.chat.id, 'Изменения на вторник успешно сохранены!')

                msg = bot.send_message(call.message.chat.id, 'Укажите, какое событие сохарнить на этот день:')
                bot.register_next_step_handler(msg, writer2_)

            elif call.data == 'wed':
                def writer3_(message):
                    global wednesday
                    wednesday = message.text
                    bot.send_message(call.message.chat.id, 'Изменения на среду успешно сохранены!')

                msg = bot.send_message(call.message.chat.id, 'Укажите, какое событие сохарнить на этот день:')
                bot.register_next_step_handler(msg, writer3_)

            elif call.data == 'thu':
                def writer4_(message):
                    global thursday
                    thursday = message.text
                    bot.send_message(call.message.chat.id, 'Изменения на четверг успешно сохранены!')

                msg = bot.send_message(call.message.chat.id, 'Укажите, какое событие сохарнить на этот день:')
                bot.register_next_step_handler(msg, writer4_)

            elif call.data == 'fri':
                def writer5_(message):
                    global friday
                    friday = message.text
                    bot.send_message(call.message.chat.id, 'Изменения на пятницу успешно сохранены!')

                msg = bot.send_message(call.message.chat.id, 'Укажите, какое событие сохарнить на этот день:')
                bot.register_next_step_handler(msg, writer5_)

            elif call.data == 'sat':
                def writer6_(message):
                    global saturday
                    saturday = message.text
                    bot.send_message(call.message.chat.id, 'Изменения на субботу успешно сохранены!')

                msg = bot.send_message(call.message.chat.id, 'Укажите, какое событие сохарнить на этот день:')
                bot.register_next_step_handler(msg, writer6_)

            elif call.data == 'sun':
                def writer7_(message):
                    global sunday
                    sunday = message.text
                    bot.send_message(call.message.chat.id, 'Изменения на воскресенье успешно сохранены!')

                msg = bot.send_message(call.message.chat.id, 'Укажите, какое событие сохарнить на этот день:')
                bot.register_next_step_handler(msg, writer7_)
            else:
                bot.send_message(call.message.chat.id, 'Где-то роизошла ошибка(')
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="На какой день вы хотите назначить событие?",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Изменения успешно сохранены. Спасибо за использование!")

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
