with open("keys.txt", "r") as textfile:
    list2 = []
    for item in textfile:
        list2.append(item + str(number))
    print list2
