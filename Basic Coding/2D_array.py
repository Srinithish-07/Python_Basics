row_num = int(input("Enter nos of rows : "))
col_num = int(input("Enter nos of coloums : "))

multi_list = [[0 for j in range(col_num)] for j in range(row_num)]

for i in range(row_num):
    row = []
    for j in range(col_num):
        row.append(0)
    multi_list.append(row)

for i in range(row_num):
    for j in range(col_num):
        multi_list[i][j]= i * j
    
for k in multi_list:
    print(k)
