import random, telebot, logging, math

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.INFO)

start_message = """Давай начнем) напиши мне команду, и я выполню её. 
Если нужна помощь, вызови /help"""

help_message = """напиши 'калькулятор' и я выведу тебе настоящий калькулятор для подсчетов.
напиши 'игра' и мы поиграем в Угадай число"""

value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data = 'no'),
                telebot.types.InlineKeyboardButton('C', callback_data = 'C'),
                telebot.types.InlineKeyboardButton('<=', callback_data = '<='),
                telebot.types.InlineKeyboardButton('/', callback_data = '/') )

keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data = '7'),
                telebot.types.InlineKeyboardButton('8', callback_data = '8'),
                telebot.types.InlineKeyboardButton('9', callback_data = '9'),
                telebot.types.InlineKeyboardButton('*', callback_data = '*') )

keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data = '4'),
                telebot.types.InlineKeyboardButton('5', callback_data = '5'),
                telebot.types.InlineKeyboardButton('6', callback_data = '6'),
                telebot.types.InlineKeyboardButton('-', callback_data = '-') )

keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data = '1'),
                telebot.types.InlineKeyboardButton('2', callback_data = '2'),
                telebot.types.InlineKeyboardButton('3', callback_data = '3'),
                telebot.types.InlineKeyboardButton('+', callback_data = '+') )

keyboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data = 'no'),
                telebot.types.InlineKeyboardButton('0', callback_data = '0'),
                telebot.types.InlineKeyboardButton(',', callback_data = '.'),
                telebot.types.InlineKeyboardButton('=', callback_data = '=') )

@bot.message_handler(commands=['start', 'help'])
def send_start(message):
    print('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    msg = None

    if message.text.lower() == '/start':
        msg = bot.send_message(message.chat.id, start_message, parse_mode='markdown')

    elif message.text.lower() == '/help':
        msg = bot.send_message(message.chat.id, help_message, parse_mode='markdown')
        
    if (msg):
        print('Бот: %s'%msg.text)
@bot.message_handler(func=lambda message: message.text.lower() == "калькулятор")
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, "0", reply_markup = keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup = keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        try:
            value = str( eval(value) )
        except:
            value = 'Ошибка!'
    else:
        value += data

    if ( value != old_value and value != '' ) or ( '0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text = '0', reply_markup = keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text = value, reply_markup = keyboard)
            old_value = value

    if value == 'Ошибка!': value = ''


storage = dict()

def exp(float_):
    return math.exp(float_)

def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]

@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def command_text_hi(m):
    bot.send_message(m.chat.id, "Привет)")

@bot.message_handler(func=lambda message: message.text.lower() == "игра")
def digitgames(message):
    init_storage(message.chat.id)
    
    attempt = 50
    set_data_storage(message.chat.id, "attempt", attempt)

    bot.send_message(message.chat.id, f'Игра "угадай число"!\nКоличество попыток: {attempt}')

    random_digit=random.randint(1, 1000)
    print(random_digit)

    set_data_storage(message.chat.id, "random_digit", random_digit)
    print(get_data_storage(message.chat.id))
 
    bot.send_message(message.chat.id, 'Готово! Загадано число от 1 до 1000!')
    bot.send_message(message.chat.id, 'Введите число:')
    bot.register_next_step_handler(message, process_digit_step)

def process_digit_step(message):
    user_digit = message.text
    
    if not user_digit.isdigit():
            msg = bot.reply_to(message, 'Вы ввели не цифры, введите пожалуйста цифры')
            bot.register_next_step_handler(msg, process_digit_step)
            return

    attempt = get_data_storage(message.chat.id)["attempt"]
    random_digit = get_data_storage(message.chat.id)["random_digit"]

    if int(user_digit) == random_digit:
        bot.send_message(message.chat.id, f'Ура! Ты угадал число! Это была цифра: {random_digit}, ты угадал его с {50 - attempt + 1} попытки!')
        init_storage(message.chat.id)
        return

    elif attempt > 1:
        attempt-=1
        set_data_storage(message.chat.id, "attempt", attempt)
        bot.send_message(message.chat.id, f'Неверно, осталось попыток: {attempt}')
        bot.register_next_step_handler(message, process_digit_step)
        if int(user_digit) > random_digit:
            bot.send_message(message.chat.id, f'Число меньше загаданного, пробуй еще')
        if int(user_digit) < random_digit:
            bot.send_message(message.chat.id, f'Число больше загаданного, пробуй еще')
    else:
        bot.send_message(message.chat.id, 'Вы проиграли!')
        init_storage(message.chat.id)
        return

bot.polling(none_stop=False, interval = 0)