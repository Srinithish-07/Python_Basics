#Write a Python program to reverse the digits of a given number and add them to the original. Repeat this procedure if the sum is not a palindrome.

def check_palindrome(number):
    count = 0
    while True:
        str_num = str(number)
        if str_num == str_num[::-1]:
            break
        else:
            rev = int(str_num[::-1])
            number += rev
            count += 1

    print(f"The final Palindrome : {number}")
    print(f"count : {count}")


original_number = int(input("Enter a number : "))
check_palindrome(original_number)





    