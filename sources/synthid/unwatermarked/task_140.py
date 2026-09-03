def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return  num1 - num2
   elif operator == '*':
        return   num1 * num2
     elif operator == '/':
         if num2 != 0:
             return num1 / num2
         else:
             return "Error! Division by zero."
     else:
         return "Invalid Operator"

# Get inputs from user
num1 = float(input("Enter first number: "))
num2 = float(input('Enter second number: '))
operator = input("Enter an operator (+,-,*,/): ")

print(calculate(num1,num2,operator))
