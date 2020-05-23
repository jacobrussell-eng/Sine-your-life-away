import numpy as np
from s1_create_the_system_of_equations import *
temp = False
import sys

top_left_matrix_A = (matrix_A.item((0, 0)))
top_right_matrix_A = (matrix_A.item((0, 1)))
bottom_left_matrix_A = (matrix_A.item((1, 0)))
bottom_right_matrix_A = (matrix_A.item((1, 1)))


top_vector_B = (vector_B.item((0, 0)))
bottom_vector_B = (vector_B.item((1, 0)))

det = (top_left_matrix_A * bottom_right_matrix_A) - (top_right_matrix_A * bottom_left_matrix_A)
if det == 0:
    print("The determinant of the first matrix is equal to 0 so finding an inverse to a cannot be done")
    sys.exit()
print('')
print('This produces a determinor of 1 /', det)
print('Which we will now multiply by the following matrix to create our inverse of matrix A')
print('')

temp_top_left_matrix_A_recip = (bottom_right_matrix_A)
temp_bottom_right_matrix_A_recip = (top_left_matrix_A)
temp_top_right_matrix_A_recip = (top_right_matrix_A * -1)
temp_bottom_left_matrix_A_recip = (bottom_left_matrix_A * -1)

temp_top_row_matrix_A_recip = np.array([[temp_top_left_matrix_A_recip, temp_top_right_matrix_A_recip]])
temp_bottom_row_matrix_A_recip = np.array([[temp_bottom_left_matrix_A_recip, temp_bottom_right_matrix_A_recip]])
temp_matrix_A_recip = np.concatenate((temp_top_row_matrix_A_recip, temp_bottom_row_matrix_A_recip), axis=0)
print(temp_matrix_A_recip)
print('')
print('This results in the following matrix - the inverse of matrix A')
print('')

top_left_matrix_A_recip = (temp_matrix_A_recip.item((0, 0)) * (1 / det))
top_right_matrix_A_recip = (temp_matrix_A_recip.item((0, 1)) * (1 / det))
bottom_left_matrix_A_recip = (temp_matrix_A_recip.item((1, 0)) * (1 / det))
bottom_right_matrix_A_recip = (temp_matrix_A_recip.item((1, 1)) * (1 / det))

top_row_matrix_A_recip = np.array([[top_left_matrix_A_recip, top_right_matrix_A_recip]])
bottom_row_matrix_A_recip = np.array([[bottom_left_matrix_A_recip, bottom_right_matrix_A_recip]])
matrix_A_recip = np.concatenate((top_row_matrix_A_recip, bottom_row_matrix_A_recip), axis=0)
print(matrix_A_recip)
print('')
print("----------------------------------------------")
print("")

top_left_identity_matrix = int((top_left_matrix_A * top_left_matrix_A_recip) + (top_right_matrix_A * bottom_left_matrix_A_recip))
top_right_identity_matrix = int((top_left_matrix_A * top_right_matrix_A_recip) + (top_right_matrix_A * bottom_right_matrix_A_recip))
bottom_left_identity_matrix = int((bottom_left_matrix_A * top_left_matrix_A_recip) + (bottom_right_matrix_A * bottom_left_matrix_A_recip))
bottom_right_identity_matrix = int((bottom_left_matrix_A * top_right_matrix_A_recip) + (bottom_right_matrix_A * bottom_right_matrix_A_recip))

answer_vector_top_row = (top_left_matrix_A_recip * top_vector_B) + (top_right_matrix_A_recip * bottom_vector_B)
answer_vector_bottom_row = (bottom_left_matrix_A_recip * top_vector_B) + (bottom_right_matrix_A_recip * bottom_vector_B)

answer_vector_top_row = np.array([[answer_vector_top_row]])
answer_vector_bottom_row = np.array([[answer_vector_bottom_row]])
answer_vector = np.concatenate((answer_vector_top_row, answer_vector_bottom_row), axis=0)
print('The top value = x')
print('The bottom value = y')
print('')
print(answer_vector)






