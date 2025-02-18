# Write a Python function greater_than(key, my_list) that checks if all elements after the first occurrence of key in my_list are greater than key.

Print "Key not present" if key is not in the list.
Print "No, all the elements are not greater than the key" if there is any element after key that is smaller than or equal to key.
Print "All elements are greater than the key" if all elements after key are greater.


def greater_than(key,my_list):
    # Edge case to handle if the key is not present
    if key not in list:
        print("Key not Present")
        return

    key_present = False
    for i in list:
        if i == key:
            key_present = True
        elif key > i and key_present:
            print("No,all the elements are not greater than the key")
            return
            
    print("All elements are greater than the key")

if __name__ == "__main__":
    n = int(input("Enter number of elements in list : "))
    list = [int(input(f"Enter element {i+1} : ")) for i in range(n)]
    print(f"\nlist : {list}")
    key = int(input("Enter the key : "))
    greater_than(key,list)
