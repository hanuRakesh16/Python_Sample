def swap(new):
    temp = newList[0]
    newList[0] = newList[-1]
    newList[-1] = temp

    return newList


newList = [1, 2, 3, 4, 5, 6, 7]

print(swap(newList))
