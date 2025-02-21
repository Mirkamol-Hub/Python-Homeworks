

#  Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
#Example:

#Input sentence: "I love apples."
#Replace: "apples"
#With: "oranges"
#Output: "I love oranges."

text = input("Enter a sentence: ")
old_word1 = input("Enter the first word to replace: ")
new_word1 = input("Enter the new word: ")
old_word2 = input("Enter the second word to replace: ")
new_word2 = input("Enter the new word: ")


updated_text = text.replace(old_word1, new_word1).replace(old_word2, new_word2)

print("Updated sentence : ", updated_text)
