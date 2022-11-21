num1 = input('Enter first number: ')  
num2 = input('Enter second number: ') 


# Arithmetic operators 
sum = float(num1) + float(num2)
min = float(num1) - float(num2) 
mul = float(num1) * float(num2) 
div = float(num1) / float(num2)
mod = float(num1) % float(num2)
exp = float(num1) ** float(num2)


# Display the sum  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))  
# Display the modulus 
print('The modulus of {0} and {1} is {2}'.format(num1, num2, mod))
# Display the exponent 
print('The exponent of {0} and {1} is {2}'.format(num1, num2, exp))