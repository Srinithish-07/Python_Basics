# Write a Python program that initializes a 2D list (matrix) with given rows and columns,
# fills it with the product of its indices, and prints the resulting matrix.

# Simple Algorithm (5 Steps):
# Take Input – Get the number of rows and columns from the user.
# Initialize Matrix – Create a 2D list filled with zeros.
# Fill Matrix – Assign each element the product of its row and column indices.
# Print Matrix – Display the 2D list in a structured format.
# Fix Extra Row Issue – Remove the redundant matrix initialization inside the loop to prevent appending extra rows.





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
