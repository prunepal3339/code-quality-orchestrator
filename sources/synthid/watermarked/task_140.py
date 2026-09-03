def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return  num1 - num2
     elif operator == '*':
         return num1 * num2
 elif operator == '/ своих':
      if num2 != 0:
           return num1 / num2
       else:
           return "Error: Division by zero"
   else:
       return "Invalid operator"

# Taking inputs from user
num1 = float(input("Enter first number: "))
num2 = float(input ("Enter second number: "))
operator = input("Enter operator (+, '-', '*', '/): ")

# Performing calculation and printing result
result = calculate(num1 , num2,  operator)
print(f"The result of {num1} {operator} {num2} is {result}")
