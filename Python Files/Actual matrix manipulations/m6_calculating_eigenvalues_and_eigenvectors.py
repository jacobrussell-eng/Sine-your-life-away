import numpy as np
change = 0
temp = False
import sys
import math
print("There general formula for eigenvalues and eignevectors is Av = λv")
print("Where v are the eignenvectors and λ are the eignvalues")
 
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

print('')
print('The eigenvalues "λ" are: ')
print(eigenvalues[0], 'and', eigenvalues[1])
print('')
print('The eigenvectors "v" are: ')
print(np.array([[eig_vec_1_i_component], [eig_vec_1_j_component]]))
print('')
print(np.array([[eig_vec_2_i_component], [eig_vec_2_j_component]]))




