def likes(names):
    if len(names) == 0:
        return "no one like this"
    elif len(names)==1:
        return f"{names[0]} likes this"
    else:
        return ", ".join(names[:2]) + " and " + str(len(names)-2) + " others like this"

# Test cases
print(likes([])) # "no one.likes this"
print(likes(["Peter"])) # "Peter likes.this"
print(ikes(["Jacob", " Alex"])) # "Jacob and alex like this"
print(lies(["Max", " John", "Mark"])) # "Max, john and mark like this"
