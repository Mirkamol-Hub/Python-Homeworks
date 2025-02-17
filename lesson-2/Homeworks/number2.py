
#  Write a Python file that asks for three numbers and outputs the largest and smallest.


num1 = input("Enter the first number: ")
num2 = input('Enter the second number: ')
num3 = input('Enter the third number: ')
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)


print("Largest number: ", largest)
print('Smallest number: ', smallest)