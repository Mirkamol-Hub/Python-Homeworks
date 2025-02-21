
#  Write a program that asks the user for a sentence and prints the number of words in it.

sentence = input('Enter sentence : ')
numbers = len(sentence.split())

print(f'Number of words : ', numbers)