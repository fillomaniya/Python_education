# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

N = int(input("Введите число N: "))
print(f'{N} ->', end= ' ')
def result(N):
    i = 2
    numbers = []
    while i * i <= N:
        while N % i == 0:
            numbers.append(i)
            N = N / i
        i += 1
    if N > 1:
        numbers.append(round(N))
    return numbers
print(result(N))

