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