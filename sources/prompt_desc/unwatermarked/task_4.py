def is_isogram(string):
    return len(set(string.lower())) == len(string.lower())

print(is_isogram("Derm Coin")) # True
print(is_isogram("aba")) # False
print(is_isogram("moOse")) # False
