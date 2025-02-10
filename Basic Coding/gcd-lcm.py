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
    
    for k in range(int(y//2),0,-1):
        if x%k == 0 and y%k == 0:
            gcd = k

    return k

print(gcd_1(84,12))