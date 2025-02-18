#python program to check whether a given number is a prime number or not
import math as m

def check_prime(number):
    if number <= 1:
        print("Not a prime number.")
    elif number == 2:
        print("Only even prime number.")
    elif number % 2 == 0:
        print("Not a prime number.")

    else:
        max_divisor = int(m.sqrt(number)) + 1
        for i in range(3,max_divisor,2):
            if number % i == 0:
                print("Not a prime number.")
                break
            else:
                print("Its a prime number..")

number = int(input("Enter an integer : "))
check_prime(number)