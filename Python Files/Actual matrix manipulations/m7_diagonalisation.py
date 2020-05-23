import numpy as np
import math
import sys

change = 0
temp = False
while change != 1:
    top_left_matrix_A = float(input("What is the top left value of matrix a?"))
    top_right_matrix_A = float(input('What is the top right value of matrix a?'))
    bottom_left_matrix_A = float(input('What is the bottom left value of matrix a?'))
    bottom_right_matrix_A = float(input('What is the bottom right value of matrix a?'))
    
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

eigenstuff = (np.linalg.eig(A))
eigenvalues = (eigenstuff[0])
eigenvectors = eigenstuff[1]

eig_val_1 = (eigenvalues[0])
eig_val_2 = (eigenvalues[1])


eig_vec_1 = (eigenvectors[0])
eig_vec_1_i_component = (eig_vec_1[0])
eig_vec_1_j_component = (eig_vec_1[1])

eig_vec_2 = (eigenvectors[1])
eig_vec_2_i_component = (eig_vec_2[0])
eig_vec_2_j_component = (eig_vec_2[1])

#Matrix D
top_left_matrix_D = (eig_val_1)
top_right_matrix_D = (0)
bottom_left_matrix_D = (0)
bottom_right_matrix_D = (eig_val_2)

D_top_row = np.array([[top_left_matrix_D, top_right_matrix_D]])
D_bottom_row = np.array([[bottom_left_matrix_D, bottom_right_matrix_D]])
D = np.concatenate((D_top_row, D_bottom_row), axis=0)

#Matrix P
top_left_matrix_P = (eig_vec_1_i_component)
top_right_matrix_P = (eig_vec_1_j_component)
bottom_left_matrix_P = (eig_vec_2_i_component)
bottom_right_matrix_P = (eig_vec_2_j_component)

P_top_row = np.array([[top_left_matrix_P, top_right_matrix_P]])
P_bottom_row = np.array([[bottom_left_matrix_P, bottom_right_matrix_P]])
P = np.concatenate((P_top_row, P_bottom_row), axis=0)

#Matrix P^-1
P_inverse = np.linalg.inv(P)


print('The matrix A can be wriiten in the form PDP^-1 where: ')
print('')
print('Matrix P:')
print(P)
print('')
print('Matrix D:')
print(D)
print('')
print('Matrix P^-1:')
print(P_inverse)
print('')









