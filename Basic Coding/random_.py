'''import random as r
list = ['a','e','i','o','u','I']
random_num = r.choice(list)
r.shuffle(list)
print(random_num)
print(''.join(list))'''


def remove_index(word,index):
    str_1 = word[:index]
    str_2 = word[index+1:]
    return str_1 + str_2
    
word = input("enter a word : ")
index = int(input("Enter the index : "))
result = remove_index(word,index)
print(result)


