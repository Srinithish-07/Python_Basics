#Write a Python program to find common divisors between two numbers in a given pair.
def common_divisor(pair):
    divisors = []
    for div in range(1,min(pair)+1):
        if pair[0] % div == 0 and pair[1] % div == 0:
            divisors.append(str(div))
    return ' '.join(divisors)

try:
    nums = input("Enter two integers (space-separated) : ")
    pair = list(map(int,nums.split()))
    if len(pair) == 2:
        result = common_divisor(pair)
        print(f"Common Divisors of {pair[0]} and {pair[1]} are : ",result)

    else:
        print("Enter only two elements..")

except ValueError:
    print("Enter a valid input..")