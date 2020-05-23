import numpy as np
change = 0
temp = False
import sys
 
while change != 1:
    top_left_matrix_A = int(input("What is the top left value of matrix a?"))
    top_right_matrix_A = int(input('What is the top right value of matrix a?'))
    bottom_left_matrix_A = int(input('What is the bottom left value of matrix a?'))
    bottom_right_matrix_A = int(input('What is the bottom right value of matrix a?'))
    
    A_top_row = np.array([[top_left_matrix_A, top_right_matrix_A]])
    A_bottom_row = np.array([[bottom_left_matrix_A, bottom_right_matrix_A]])
    A = np.concatenate((A_top_row, A_bottom_row), axis=0)
    print('Here is the matrix you just created')
    print('')
    print(A)
    print('')
    temp = False
    while temp != True:
        choice_1 = input('Would you like to re-assign the values of the matrix you just created Y/N?')
        if choice_1 == 'N':
            temp = True
            change = 1
        elif choice_1 == 'Y':
            temp = True
        else:
            print('Not a valid answer, try again')

det = (top_left_matrix_A * bottom_right_matrix_A) - (top_right_matrix_A * bottom_left_matrix_A)

temp_top_left_matrix_A_recip = (bottom_right_matrix_A)
temp_bottom_right_matrix_A_recip = (top_left_matrix_A)
temp_top_right_matrix_A_recip = (top_right_matrix_A * -1)
temp_bottom_left_matrix_A_recip = (bottom_left_matrix_A * -1)

temp_top_row_matrix_A_recip = np.array([[temp_top_left_matrix_A_recip, temp_top_right_matrix_A_recip]])
temp_bottom_row_matrix_A_recip = np.array([[temp_bottom_left_matrix_A_recip, temp_bottom_right_matrix_A_recip]])
temp_matrix_A_recip = np.concatenate((temp_top_row_matrix_A_recip, temp_bottom_row_matrix_A_recip), axis=0)

print('Below is the inverse of matrix A')
print('')

if det != 0:
    top_left_matrix_A_recip = (temp_matrix_A_recip.item((0, 0)) * (1 / det))
    top_right_matrix_A_recip = (temp_matrix_A_recip.item((0, 1)) * (1 / det))
    bottom_left_matrix_A_recip = (temp_matrix_A_recip.item((1, 0)) * (1 / det))
    bottom_right_matrix_A_recip = (temp_matrix_A_recip.item((1, 1)) * (1 / det))


    top_row_matrix_A_recip = np.array([[top_left_matrix_A_recip, top_right_matrix_A_recip]])
    bottom_row_matrix_A_recip = np.array([[bottom_left_matrix_A_recip, bottom_right_matrix_A_recip]])
    matrix_A_recip = np.concatenate((top_row_matrix_A_recip, bottom_row_matrix_A_recip), axis=0)
    print(matrix_A_recip)
    print('')

else:
    print("Determinant is zero, therefore operation is invalid")