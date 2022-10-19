# В файле находятся названия фруктов. Выведите все фрукты, 
# названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

data = open('python/seminar_3/fruit.txt')
text = data.readlines()
print(text)
list = []
print('Введите первую букву (заглавную) названия фрукта: ')
letter = input()
print(f'{letter} -> ')
for i in text:
    if i[0] == letter:
        list.append(i)
for j in range(len(list)):
    print(list[j], end = '')