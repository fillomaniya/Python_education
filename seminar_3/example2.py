def Number():
    num = open('python/seminar_3/text2.txt')
    point = num.readlines()
    num.close()
    for i in range(0,len(point),2):
        print(point[i], end= "")
    print()
    for j in range(1,len(point),2):
        print(point[j], end= "")
Number()