# Даны две строки. Посчитайте сколько 
# раз каждый символ первой строки встречается 
# во второй «one» «onetwonine» - o – 2, n – 3, e – 2

str1 = "one"
str2 = "onetwonine"
print(f"{str1}, {str2}")

for i in str1:
    count = str2.count(i)
    if count > 1:
        print (f'{i} - {count} ', end = ' ')