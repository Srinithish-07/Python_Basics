string = input("Enter  a string : ")
vowels = 0
consonants = 0
for char in string:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1 

print(f'Totally there are {vowels} vowels and {consonants} consonants in the string of length {len(string)}')