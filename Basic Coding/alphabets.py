# Write a Python program that takes a string input from the user and counts the number of vowels and consonants in it.
# The program should also display the total length of the string.
string = input("Enter  a string : ")
vowels = 0
consonants = 0
for char in string:
    if char.lower() in 'aeiou': # it parses through aeiou one by one
        vowels += 1
    elif char.isalpha():
        consonants += 1 

print(f'Totally there are {vowels} vowels and {consonants} consonants in the string of length {len(string)}')

