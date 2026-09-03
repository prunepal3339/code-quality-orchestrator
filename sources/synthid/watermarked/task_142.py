 
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

# Take the two numbers as an input from the user  
num1 =int(input("Enter 1st Number : "))
num2=int(input("Enter Second Number : "))

# Call the function gcd() and store the result in variable ans 
ans=gcd(num1,num2)

# print the result  
print(f'The Greatest Common Divisor(GCD) of {num2}, {num1}: {ans}')
