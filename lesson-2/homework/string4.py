

#  Write a Python program to check if a given string is palindrome or not.

#What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.

my_string = input('Eneter an word: ')


if my_string== my_string[::-1]:
  print(f'{my_string} is a palindrome word.')

else:
  print(f'{my_string} is not a palindrome word.')
