#Exercise 1: character inspector

# word = input("Enter a word: ")
# print("First character: ",word[0])
# print("Last character: ",word[-1])
# print("Length of the word: ",len(word))

#Exercise 2: Name Formatter

# name = input("Enter your full name: ").strip().title()
# print(name)

#Exercise 3: vowel counter

# text = input("Enter text: ").lower()
# vowels = "aeiou"
# count = 0
# for char in text:
#     if char in vowels:
#         count += 1
# print("Vowels:", count)


#Exercise 4: Reverse Checker

# word = input("Enter a word: ").strip()
# print("Original: ",word)
# print("Reversed: ",word[::-1])

#Exercise 5: palindrome checker

# word = input("Enter a word:").strip().lower()
# if word == word[::-1]:
#     print("Palindrome: ","Yes")
# else:
#     print("Palindrome:","No")

#Exercise 6: character frequency

text = input("Enter text:").strip()
character = input("Enter character:").lower()
count = 0
for char in text:
    if char.lower() == character:
        count += 1
print(character, "appears",count,"times")