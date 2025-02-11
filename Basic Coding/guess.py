import random as r

def guess_num():
    user_input = int(input("\nGuess the number (1 to 10) : "))
    random_num = r.randint(1,10)
    if user_input == random_num:
        print("Hooray! , u guessed correctly")
    else:
        print("Oops wrong Guess , Try again..")
        guess_num() #recursively called to avoid again running the code
        # Can use while loop also but recursive call is much les time complexity

guess_num()

