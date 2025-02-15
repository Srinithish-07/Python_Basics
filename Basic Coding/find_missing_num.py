# Write a Python function that takes a phone number as input and determines which digits (0-9) are missing from it.
# Ensure that the function handles invalid inputs gracefully

def find_missing_digits(phone_number):
    phone_digits = set(str(phone_number)) # difference in set can give the missing nums in given input
    all_digits = set('0123456789')
    missing_digits = all_digits  - phone_digits
    return missing_digits

try:
    phone_number = int(input("Enter the phone number : "))
    missing_digits = find_missing_digits(phone_number)

    if missing_digits:
        print(f"Missing digits : {','.join(sorted(missing_digits))}")
    else:
        print("All numbers are present in the phone number")

except ValueError:
    print("Invalid input , enter a valid phone number")

    
