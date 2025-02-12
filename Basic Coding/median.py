def sorting(my_list): # Bubble sorting - sorting largest to last position by using loop
    n = len(my_list)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
                swapped = True
        if swapped == False:
            break
    return my_list

def median(my_list):
    n = len(my_list)
    if n%2 == 0:
        middle_1 = my_list[n//2]
        middle_2 = my_list[(n//2)-1]
        median   = (middle_1 + middle_2)/2
    else:
        median = my_list[n//2]

    return median

n = int(input("Enter length of list : "))
my_list = []
for i in range(n):
    element = int(input(f"Enter element {i+1} : "))
    my_list.append(element)

print(f"List : {my_list}")
sorted_list = sorting(my_list.copy()) # using user-defined function
#my_list = sorted(my_list) // using sorted function
print(f"Sorted List : {sorted_list}")
result = median(sorted_list)
print(f"median of list {sorted_list} : {result}")

