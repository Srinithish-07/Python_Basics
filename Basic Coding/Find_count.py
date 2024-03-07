my_list = []
size = int(input("enter limit of list : "))
for i in range(size):
    element = int(input(f"Enter {i} element : "))
    my_list.append(element)

key = int(input("enter a key : "))
count = 0
for i in my_list:
    if key == i:
        count += 1
print(f"the number {key} present in list is {count} times")
