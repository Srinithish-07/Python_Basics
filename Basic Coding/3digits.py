#Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
for i in range(100,401):
    str_num = str(i)
    if(int(str_num[0])%2==0 and int(str_num[1])%2==0 and int(str_num[2])%2==0):
        print(str_num,end=',')
        