'''getting inputs for list using map'''
nums = input("Enter space-separated elements : ")
my_list = list(map(int,nums.split()))
print(my_list)

'''getting input for list using for loop'''
n = int(input("enter n : "))
a_list = []
for i in range(n):
    element = input(f"enter element {i+1} : ")
    a_list.append(element)
print(a_list)

print(type(my_list))
print(type(a_list))


