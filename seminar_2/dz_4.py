# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Сдвиньте все элементы списка 
# на 2 позиции вправо. 3 -> [2, 3, -3, -2, -1, 0, 1]
print("Введите число N для списка [-N,N]: ")
N = int(input())
list = []
for i in range(-N,N+1):
    list.append(i)
print(list)
print("Введите число, на которое нужен сдвиг вправо: ")
shift = int(input())

result = list[-shift:] + list[:-shift]

print(result)

