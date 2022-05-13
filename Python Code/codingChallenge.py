twoDigitNumber = input("Enter the number: ")
firstNumber = twoDigitNumber[0] # subscripting
secondNumber = twoDigitNumber[1] # subscripting
result = int(firstNumber) + int(secondNumber) # typecasting
print("The sum is: "+str(result)) 
# you cannot concatenate different data types -> str cannot be concatenated with int