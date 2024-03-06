'''distance between two points using x1,x2,y1,y2 variables'''
import math as m
'''def distance():
    x1 = int(input("Enter x1 : "))
    y1 = int(input("Enter y1 : "))
    x2 = int(input("Enter x2 : "))
    y2 = int(input("Enter y2 : "))

    distance = round(m.sqrt((x2-x1)**2 + (y2-y1)**2),4)

    return distance

print(distance())'''

'''or directly giving input as list'''
def distance():
    p1 = [int(input(f"Enter element {i} of p1 : "))for i in range(2)]
    p2 = [int(input(f"Enter element {i} of p2 : "))for i in range(2)]

    distance = round(m.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2),4)
    print("The distance between the points {} and {} are : {}".format(p1,p2,distance))
    return 0

print(distance())