# В зоопарк отправили отчёт о новом поступлении
# зверей с ошибкой, в результате которой некоторые данные не
# расшифровались. Расшифруйте данные. Определите, в какой
# клетке находится лев. Номер клетки совпадает с номером
# строки.

def ConvertToBinary(number):
    result = ''
    while number > 0:
        result = str(number%2) + result
        number = number // 2
    return result

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

codelist = [ConvertToBinary(i) for i in range(len(alphabet))]
codelist = ["0"*(6-len(i)) + i for i in codelist]

dictionary = {}
for i in range(len(codelist)):
    dictionary[codelist[i]] = alphabet[i]
print(dictionary)

data = open('python/seminar_5/animals.txt', 'r')
animalsCodeList = data.readlines()
data.close()

for animal in animalsCodeList:
    for i in range(len(animal)//6):
        bias = i * 6
        print(dictionary[animal[bias:bias+6]], end = '')
    print()
