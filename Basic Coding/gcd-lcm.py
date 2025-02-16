# What are the differences between using the math module
# and a manual approach to calculate the GCD and LCM of two numbers in Python?
# Which method is more efficient, and why?

'''fiirst type using math module'''
import math as m
def gcd(x,y):
    return m.gcd(x,y)

def lcm(x,y):
    return abs(x*y)//m.gcd(x,y)

print(gcd(98,22))
print(lcm(98,22))

'''using normal formula'''

def gcd_1(x,y):
    gcd = 1
    if x % y == 0:
        return y
    
    for k in range(int(y//2),0,-1):    #The loop starts from y//2 and decreases down to 1.
        if x%k == 0 and y%k == 0:      ## Since the highest possible GCD (other than y itself) is at most y//2, this reduces the number of iterations.
            gcd = k                                
    return k

print(gcd_1(84,12))
