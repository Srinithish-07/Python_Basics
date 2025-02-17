from itertools import permutations as p
nums = input("enter space-separated numbers : ")
my_list = list(map(int , nums.split()))
print(f"List : {my_list}")
permutated_list = list(p(my_list,3))
print(f"permutated_list : {permutated_list}")
