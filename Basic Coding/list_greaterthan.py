def greater_than(key,my_list):
    key_present = False
    for i in my_list:
        if key == i:
            key_present = True

        elif key > i and key_present == True:
            print("No,all the elements are not greater than the key")
            return
    
    if not key_present:
        print("key not present")
    else:
        print("All elements are greater than the key")


n = int(input("Enter number of elements in list : "))
list = []
for i in range(n):
    element = int(input(f"Enter element {i+1} : "))
    list.append(element)
print(f"\nlist : {list}")
key = int(input("Enter the key : "))
greater_than(key,list)