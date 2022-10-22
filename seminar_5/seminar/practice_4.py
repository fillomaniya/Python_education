# Имеется информация о том, телефонами
# каких компаний сейчас торгуют магазины.
# Определите те компании, чьи телефоны
# присутствуют в каждом магазине

data = open('python/seminar_5/Телефоны.txt', 'r')
phones = data.readlines()
data.close()

shopF = set(phones[1].replace('\n', '').split(', '))
shopS = set(phones[3].replace('\n', '').split(', '))
shopT = set(phones[5].split(', '))
print(shopF.intersection(shopS).intersection(shopT))
