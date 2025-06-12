def calculate_counts(word):
    letters = digits = spaces = 0 # chained assignment
    for char in word:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        elif char == " ":
            spaces += 1

    print(f"Letters : {letters}\nDigits : {digits}\nspaces : {spaces}")

word = input("Enter a string : ")
calculate_counts(word)




