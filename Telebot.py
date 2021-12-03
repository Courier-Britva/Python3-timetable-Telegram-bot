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
    item1 = types.KeyboardButton("Timetable")
    item2 = types.KeyboardButton("Change Schedule")
    item3 = types.KeyboardButton("Contact the author")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Welcome, {0.first_name}!\nЯ - <b>{1.first_name}</b>, A bot for working with schedules.".format(
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

    week = ["Monday: \n" + str(monday) + "\n\nTuesday: \n" + str(tuesday) + "\n\nWednesday: \n" + str(
        wednesday) + "\n\nThursday: \n" + str(thursday) + "\n\nFriday: \n" + str(friday) + "\n\nSaturday: \n" + str(
        saturday) + "\n\nSunday:\n" + str(sunday)]

    if message.chat.type == 'private':
        if message.text == 'Timetable':
            bot.send_message(message.chat.id, week)

        elif message.text == 'Change Schedule':

            markup = types.InlineKeyboardMarkup(row_width=7)
            item1 = types.InlineKeyboardButton("Monday", callback_data='mon')
            item2 = types.InlineKeyboardButton("Tuesday", callback_data='tue')
            item3 = types.InlineKeyboardButton("Wednesday", callback_data='wed')
            item4 = types.InlineKeyboardButton("Thursday", callback_data='thu')
            item5 = types.InlineKeyboardButton("Friday", callback_data='fri')
            item6 = types.InlineKeyboardButton("Saturday", callback_data='sat')
            item7 = types.InlineKeyboardButton("Sunday", callback_data='sun')
            markup.add(item1, item2, item3, item4, item5, item6, item7)

            bot.send_message(message.chat.id, 'What day do you want to schedule the event?', reply_markup=markup)
        elif message.text == 'Contact the author':
            bot.send_message(message.chat.id, "Telegram: \n@Courier_Britva")
        else:
            bot.send_message(message.chat.id, "I don't know what to tell you 😢\n enter the command '/start' to get started")


# this function is responsible for setting a new event for each day of the week
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'mon':
                def writer1_(message):
                    global monday
                    monday = message.text
                    bot.send_message(call.message.chat.id, 'The changes for Monday have been successfully saved!')

                msg = bot.send_message(call.message.chat.id, 'Specify which event to save for that day:')
                bot.register_next_step_handler(msg, writer1_)

            elif call.data == 'tue':
                def writer2_(message):
                    global tuesday
                    tuesday = message.text
                    bot.send_message(call.message.chat.id, 'The changes for Tuesday have been successfully saved!')

                msg = bot.send_message(call.message.chat.id, 'Specify which event to save for that day:')
                bot.register_next_step_handler(msg, writer2_)

            elif call.data == 'wed':
                def writer3_(message):
                    global wednesday
                    wednesday = message.text
                    bot.send_message(call.message.chat.id, 'The changes for Wednesday have been successfully saved!')

                msg = bot.send_message(call.message.chat.id, 'Specify which event to save for that day:')
                bot.register_next_step_handler(msg, writer3_)

            elif call.data == 'thu':
                def writer4_(message):
                    global thursday
                    thursday = message.text
                    bot.send_message(call.message.chat.id, 'The changes for Thursday have been successfully saved!')

                msg = bot.send_message(call.message.chat.id, 'Specify which event to save for that day:')
                bot.register_next_step_handler(msg, writer4_)

            elif call.data == 'fri':
                def writer5_(message):
                    global friday
                    friday = message.text
                    bot.send_message(call.message.chat.id, 'The changes for Friday have been successfully saved!')

                msg = bot.send_message(call.message.chat.id, 'Specify which event to save for that day:')
                bot.register_next_step_handler(msg, writer5_)

            elif call.data == 'sat':
                def writer6_(message):
                    global saturday
                    saturday = message.text
                    bot.send_message(call.message.chat.id, 'The changes for Saturday have been successfully saved!')

                msg = bot.send_message(call.message.chat.id, 'Specify which event to save for that day:')
                bot.register_next_step_handler(msg, writer6_)

            elif call.data == 'sun':
                def writer7_(message):
                    global sunday
                    sunday = message.text
                    bot.send_message(call.message.chat.id, 'The changes for Sunday have been successfully saved!')

                msg = bot.send_message(call.message.chat.id, 'Specify which event to save for that day:')
                bot.register_next_step_handler(msg, writer7_)
            else:
                bot.send_message(call.message.chat.id, 'Theres a mistake somewhere(')
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="What day do you want to schedule the event?",
                                  reply_markup=None)


    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
