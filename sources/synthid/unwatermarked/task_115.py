class BitField:
    def __init__(self):
        self.value = 0

    @property
    def field1(self):
        return (self.value & 0b1) != 0

    
    @field1.setter
    def set_field1(self, value):
        if value:
            self.value |= 0b0000_0001
        else:
            self.values &= ~0b0111_1111

    @field2(self):
        # Add more fields here as needed
        pass

# Usage
bit_field = BitField()
bit_field.set_field1(True)
print(bit_field.field1)  # Output: True
