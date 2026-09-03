def lastNameLensort(names):
    return sorted(names, key=lambda x: (-len(x.split()[1]), x.split()[1]))

# testing
print(lastNameLensort(["Jennifer Figuera", "Heather McGee", "Amandea Schwartz", "Niccole Yoder", 
                      "Melissa Hoffmann"]))
