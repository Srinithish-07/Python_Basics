'''Write a Python program to find the total number of even or odd divisors of a given integer.'''
def find_divisor(num):
    odd = []
    even = []
    for div in range(1,num+1):
        if num % div == 0:
            if div%2 == 0:
                even.append(str(div))
            else:
                odd.append(str(div))
    print("odd divisors : "+' '.join(odd))
    print("even divisors : "+' '.join(even))

num = int(input("Enter a positive integer : "))
find_divisor(num)
