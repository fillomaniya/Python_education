#  В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки
# заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с
# наилучшим средним баллом

from random import randint

list_group = []

students = [20, 30]
score = [2, 5]
numberGroups = int(input("Введите кол-во групп: "))

for group in range(1, numberGroups + 1):
    number_students = randint(*students) 
    print(f'группа {group} ({number_students} студентов)')
    list_scores = [randint(*score) for _ in range(number_students)]
    print(list_scores)
    middle_score = sum(list_scores) / len(list_scores)
    list_group.append((f'{group}', round(middle_score, 2)))
    
x = sorted(list_group, key = lambda x : x[1])
print(x)
print(f'ответ: группа {x[-1][0]}')

