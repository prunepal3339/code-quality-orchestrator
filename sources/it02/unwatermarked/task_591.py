def swap_List(newList):
_streams = newList[0]
newList[0] = newList[-1]
newList[-1] = _streams
return newList
