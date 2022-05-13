# String
num1 = "1234" # this is still treated as a string
num2 = "5678"
sum = num1 + num2 # String concantenation is done
print(sum) # String 'sum' is returned
# Integer
print(123_456+123_456) # Add underscore for large numbers for our better understanding
# Float
print(3.1415)
# Boolean
True, False
x = range(6) # returns only integer
print(x)

numChar = len(input("What is your name?\n"))
newNumChar = str(numChar)  # Type Casting
print("Your name has "+newNumChar+" Characters")
print(type(newNumChar))

a = str(123)
print(type(a))