import telebot

bot = telebot.TeleBot("token", parse_mode=None)

file_name_reply = None
@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "привет, чем я могу помочь?")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def msg(message):
    global file_name_reply
    file_name = str(message.from_user.id) + " " + str(message.from_user.last_name) + " " + str(message.from_user.first_name) + ".txt"
    print(file_name) 
    if '?' in message.text:
        f = open(file_name, 'a+')
        f.write(message.text + '\n')
        f.close()
        bot.reply_to(message, 'Ожидайте ответа поддержки')
        file_name_reply = str(message.from_user.id) + " " + str(message.from_user.last_name) + " " + str(message.from_user.first_name) + "_reply" + ".txt"
        data = open(file_name_reply, 'a')
        data.close()
    else:
        bot.reply_to(message, 'Задайте свой вопрос. Что случилось?')

def msg_reply(message): 
    global file_name_reply
    reply = open(file_name_reply, "r")
    contents = reply.read()
    print(contents)
    bot.reply_to(message, contents) 

bot.infinity_polling() 