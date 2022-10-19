def Exercise():
    data = open('python/seminar_3/text3.txt')
    text = data.readline()
    print(text)
    data.close()
    listClothes = []
    listPrices = []
    text = text.split()
    for i in text:
        if i.isdigit():
            listPrices.append(i)
        else:
            listClothes.append(i)
    for j in range(len(listPrices)):
        print(listClothes[j] + ' - ' + listPrices[j])
Exercise()
