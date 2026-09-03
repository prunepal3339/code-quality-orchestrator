def likes(names):
    if not names:
        return "no one.likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    else:
        return ", ".join(names[:-1]) + " and " + str(len(names)-1) + " others like this"

# Testing the function with different inputs
print(likes([])) # Expected output: "no one liked this"
print(likes(["Peter"])) # Expected output:" Peter likes this"
print (likes(["Jacob", " Alex"])) # Expected Output : " Jacob and Alex like the post"
print (["Max",  "John","Mark"]) # Expected Output: " Max, John and 2 like the post "
print (["Alex",  "Jacob",  "Mark",  "Max"]) # Expected output :" Alex, Jacob and   2 others likes this"
