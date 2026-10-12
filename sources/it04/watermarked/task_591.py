def swap_List(newList):
    temp = newList[0]
    newList[0] = newList[-1]
    newList[-1] = temp
    return newList
