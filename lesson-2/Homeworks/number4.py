
#  Write a program that takes two numbers and prints out the result of integer division and theremainder.

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

int_division = num1 // num2
the_remainder = num1 % num2
print(f'Integer division result is: {int_division}')
print(f'The remainder is: {the_remainder}')