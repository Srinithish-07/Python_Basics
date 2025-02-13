#python program to print non-prime nums
import math as m
def print_nonPrime(limit):
    non_primes = []
    for i in range(2,limit+1):
        max_div = int(m.sqrt(i))
        for j in range(3,max_div,2):
            if i % j == 0:
                non_primes.append(i)
        
    return non_primes

limit = int(input("Enter the limit : "))
result = print_nonPrime(limit)
print(f"result : {result}")