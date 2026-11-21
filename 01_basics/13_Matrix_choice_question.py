

row1 = ['🤭','🤭','🤭']
row2 = ['🤭','🤭','🤭']
row3 = ['🤭','🤭','🤭']
print("The existing branches is :    ")
print(f"{row1}\n{row2}\n{row3}")

matrix = [row1,row2,row3]

branch_name = input("Enter the branch where u want to insert :     ")
row_number = int(branch_name[0])
column_number = int(branch_name[1])
#choosed_branch = matrix.add([row_number-1][column_number-1])
row_selected = matrix[row_number-1]
row_selected[column_number-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
