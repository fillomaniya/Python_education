def Dictionary():
    data = open("python/seminar_3/instruction.txt")
    string1 = data.read()
    data.close
    new_dictionary = {}
    print(string1)
    for i in string1:
        new_dictionary[i] = i
    print(new_dictionary)
Dictionary()