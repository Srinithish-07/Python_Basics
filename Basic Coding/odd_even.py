# Write a Python program that iterates through a given list of numbers and separates them into two lists:
# one containing odd numbers and the other containing even numbers.
# The program should then print the odd numbers as a comma-separated string followed by the even numbers as a comma-separated string.
list = [1,2,3,4,5,6,7,8,9,10]
odd = []
even = []
for i in list:
    if i%2==0:
        even.append(str(i))
    else:
        odd.append(str(i))

print(','.join(odd))
print(','.join(even))
