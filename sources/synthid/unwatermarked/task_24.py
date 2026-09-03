 
print(validate_pin("123")) # Returns False
print(validate_pin('123')) # Returns False

print(validate_pin(123)) # Returns False, because the input is an integer, not a string

print(validate_PIN("12a4")) # Returns True

print(validate_Pin("1245678")) # Returns false

print(validate_PIn("12")) # Returns true

print(validatePin("122333")) #Returns true

print(validePin("1111")) #Returns True
