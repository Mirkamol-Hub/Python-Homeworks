
#  Create a program that converts kilometers to meters and centimeters.

kilometers = int(input("Enter distance in kilometres: "))

meters = kilometers * 1000
centimeters = kilometers * 100000
print(f'{kilometers} kilometers are equal to: ')
print(f'{meters} meters')
print(f'{centimeters} centimetres')