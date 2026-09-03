 
def validate_pin_new(pin):
    return len(str(pin)) == 4 and str(pin).isdigit() 

# Test cases 
print(validate_pin_new(123))       # Returns True (since '123' is a string in this context)
print(validate_pin(12))          # Returns False (since '2' is out of range)
print(validate_PIN(1200))        # Returns True
print(validate_Pin('-123'))      # Return False
