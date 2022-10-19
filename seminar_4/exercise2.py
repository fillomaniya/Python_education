# Актёров разделили на списки по трём качествам
# «умные», «красивые», «сильные». На главную роль нужен актёр
# обладающий всеми тремя качествами. Определите, сколько есть
# претендентов на главную роль. Списки актёров поместите в
# соответствующие файлы

# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад

handsome = set()
smart = set()
strong = set()

with open('python/seminar_4/handsome.txt') as inf:
    for line in inf.readlines():
        handsome.add(line.rstrip())
print(handsome)

with open('python/seminar_4/smart.txt') as inf:
    for line in inf.readlines():
        smart.add(line.rstrip())
print(smart)

with open('python/seminar_4/strong.txt') as inf:
    for line in inf.readlines():
        strong.add(line.rstrip())
print(strong)

print(*(handsome & smart & strong), sep ='\n')

for el in handsome & smart & strong:
    print(el)
#------------------------------------
# первый способ преподавателя

# def openFile(nameFile):
#     f = open(nameFile)
#     phrase = f.readlines()
#     f.close()
#     list = phrase[0].split()
#     return set(list)

# handsome = openFile('python/seminar_4/handsome.txt')
# smart = openFile('python/seminar_4/smart.txt')
# strong = openFile('python/seminar_4/strong.txt')

# print(handsome.intersection(smart).intersection(strong))