import numpy as np
temp = False

change = 0
while change != 1:
    top_equation_xs = int(input('How many x\'s are their in the first equation?'))
    top_equation_ys = int(input('How many y\'s are their in the first equation?'))
    bottom_equation_xs = int(input('How many x\'s are their in the second equation?'))
    bottom_equation_ys = int(input('How many y\'s are their in the second equation?'))

    matrix_A_top_row = np.array([[top_equation_xs, top_equation_ys]])
    matrix_A_bottom_row = np.array([[bottom_equation_xs, bottom_equation_ys]])
    matrix_A = np.concatenate((matrix_A_top_row, matrix_A_bottom_row), axis=0)
    print('Here is the matrix you just created')
    print('')
    print(matrix_A)
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


change = 0
while change != 2:
    top_equation_number = int(input('What is the number at the end of the first equation?'))
    bottom_equation_number = int(input('What is the number at the end of the second equation?'))

    vector_B_top_row = np.array([[top_equation_number]])
    vector_B_bottom_row = np.array([[bottom_equation_number]])
    vector_B = np.concatenate((vector_B_top_row, vector_B_bottom_row), axis=0)
    print('Here is the vector you just created')
    print('')
    print(vector_B)
    print('')
    temp = False
    while temp != True:
        choice_1 = input('Would you like to re-assign the values of the vector you just created Y/N?')
        if choice_1 == 'N':
            temp = True
            change = 2
        elif choice_1 == 'Y':
            temp = True
        else:
            print('Not a valid answer, try again')





