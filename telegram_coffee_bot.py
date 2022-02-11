import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(
    token=config("TOKEN_BOT")
)


@bot.message_handler(commands=["start", "hi", "Hi"])
def answer_start(message):
    print(message.from_user.id)
    text = f"Welcome to bot {message.from_user.first_name}" \
           f" {message.from_user.last_name}!" \
           f" Choose the course you want to attend."
    keyboard_in = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text="Python", callback_data="python")
    btn_2 = types.InlineKeyboardButton(text="Java", callback_data="java")
    keyboard_in.add(btn_1, btn_2)

    bot.send_message(message.chat.id, text, reply_markup=keyboard_in)


@bot.callback_query_handler(func=lambda call: True)
def send_course(call):
    if call.data == "python":
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Python morning")
        btn_2 = types.KeyboardButton("Python evening")
        btn_3 = types.KeyboardButton("Python bootcamp")
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f"You chose {call.data}!"
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply)
    elif call.data == "java":
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Java morning")
        btn_2 = types.KeyboardButton("Java evening")
        btn_3 = types.KeyboardButton("Java bootcamp")
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f"You chose {call.data}!"
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply)


@bot.message_handler(content_types=["text"])
def send_good_message(message):
    if message.text == "Python morning":
        bot.send_message(
            message.chat.id,
            "You have been submitted to the course python morning! "
            "Manager will contact you!")
    elif message.text == "Python evening":
        bot.send_message(
            message.chat.id,
            "Python evening, Yay!"
        )
    elif message.text == "Python bootcamp":
        bot.send_message(
            message.chat.id,
            "Wow, you chose python bootcamp!!"
        )
    elif message.text == "Java morning":
        bot.send_message(
            message.chat.id,
            "You have been submitted to the course java morning! "
            "Manager will contact you!")
    elif message.text == "Java evening":
        bot.send_message(
            message.chat.id,
            "Java evening, Yay!"
        )
    elif message.text == "Java bootcamp":
        bot.send_message(
            message.chat.id,
            "Wow, you chose java bootcamp!!"
        )


bot.polling()
# git init - connects the folder with git repository
# git status - shows the status of the file
# git add (name of the file)
# git add . (adds every file)
# git rm --cached (.filename) - will not upload on git
# git reset --hard HEAD - откат
# rm - rf .git - deletes git
# git pull - pulls deleted branch