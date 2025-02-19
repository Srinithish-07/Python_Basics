import math as m
def sum_of_primes(limit):
    primes = []
    for i in range(2,limit+1):
        is_prime = True
        if i == 2:
            primes.append(i)
        elif i % 2 == 0:
            continue
        else:
            max_div = int(m.sqrt(i))+1
            for j in range(3,max_div,2):
                if i % j == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(i)

    return sum(primes) , len(primes)

limit = int(input("Enter the limit : "))
result1, result2 = sum_of_primes(limit)
print(f"Sum of the prime number less than {limit} : {result1}")
print(f"nos. of prime number less than {limit} : {result2}")