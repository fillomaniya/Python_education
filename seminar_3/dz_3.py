# Создайте скрипт бота, который находит ответы на 
# фразы по ключу в словаре. Бот должен, как минимум, 
# отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

my_dict = {'Привет': 'Привет', 'Как тебя зовут?': 'Анатолий', 
'Приятно познакомиться': 'Оу! мне тоже!', 
'Что ты можешь?': 'Пока что только рассказывать анекдоты', 
'Расскажи анекдот': 'Колобок повесился :('}

while True:
    enter = input('Я: ')
    if enter == '/exit':
        break
    if enter in my_dict.keys():
        print('Анатолий:', my_dict[enter])
    else:
        print('Анатолий: Повтори, я не понимаю')
