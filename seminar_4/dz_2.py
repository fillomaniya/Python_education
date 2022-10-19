# В первой строке файла находится информация об ассортименте 
# мороженного, во второй - информация о том, какое мороженное 
# есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

data = open('python/seminar_4/assortment.txt')
textAssort = data.readline()
data.close()
textAssort = textAssort.split(', ')
textAssort = set(textAssort)

data2 = open('python/seminar_4/in_stock.txt')
textStock = data2.readline()
data.close()
textStock = textStock.split(', ')
textStock = set(textStock)

print(textAssort)
print(textStock)

print('Закончилось: ', end= " ")
print(textAssort.difference(textStock))
