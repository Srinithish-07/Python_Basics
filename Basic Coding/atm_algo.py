'''Write a Python program to find the number of notes
(Samples of notes: 10, 20, 50, 100, 200, 500) against an amount.'''

'''def amount_sort(total_amount):
    original_amount = total_amount
    if total_amount != 0:
        denom_500 = total_amount // 500
        total_amount %= 500
        denom_200 = total_amount // 200
        total_amount %= 200
        denom_100 = total_amount // 100
        total_amount %= 100
        denom_50 = total_amount // 50
        total_amount %= 50
        denom_20 = total_amount // 20
        total_amount %= 20
        denom_10 = total_amount // 10
        total_amount %= 10
        denom_5 = total_amount // 5
        total_amount %= 5
        denom_1 = total_amount

    return(f"Total amount = {original_amount}\n  denom_500 - {denom_500}\n  denom_200 - {denom_200}\n  denom_100 - {denom_100}\n  denom_50  - {denom_50}\n  denom_20  - {denom_20}\n  denom_10  - {denom_10}\n  denom_5   - {denom_5}\n  denom_1   - {denom_1}")


total_amount = int(input("Enter the amount : "))
result = amount_sort(total_amount)
print(result)'''



'''using list and loop to solving'''
# advantage of list usage
def amount_sort(total_amount):
    amount_list = [500,200,100,50,20,10,5,1]
    count = []
    for denom in amount_list:
        nos = total_amount // denom
        count.append(nos)
        total_amount %= denom

        if total_amount == 0:
            break

    total_count = sum(count)

    for denom , nos in zip(amount_list,count):
        print(f"{denom} : {nos}")

    print(f"Total count : {total_count}")

total_amount = int(input("Enter total amount : "))
amount_sort(total_amount)

