def ReadLastRow():
    data = open('python/seminar_3/text.txt')
    print(data)
    text = data.readlines()
    print(text[-1])
    data.close()