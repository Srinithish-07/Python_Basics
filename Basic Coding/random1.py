#Remove duplicates from a list without using a set.
def remove(my_list):
    unique = []
    duplicate = []
    for i in my_list:
        if i not in unique:
            unique.append(i)
        else:
            duplicate.append(i)
    print(f"unique elements : {' '.join(sorted(map(str,unique)))}")
    print(f"duplicate elements : {' '.join(set(map(str,duplicate)))}")       
    
my_list = [1,5,9,6,7,1,2,3,5,4,6,9,7,8,7]
remove(my_list)



