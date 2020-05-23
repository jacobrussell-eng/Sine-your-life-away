import numpy as np
temp = False
change = 0
import sys
 
while change != 1:
    TL_A = int(input("What is the top left value of matrix a?"))
    TR_A = int(input('What is the top right value of matrix a?'))
    BL_A = int(input('What is the bottom left value of matrix a?'))
    BR_A = int(input('What is the bottom right value of matrix a?'))
    
    A_top_row = np.array([[TL_A, TR_A]])
    A_bottom_row = np.array([[BL_A, BR_A]])
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


        
    
    
change = 0
while change != 2:
    TL_B = int(input("What is the top left value of matrix b?"))
    TR_B = int(input('What is the top right value of matrix b?'))
    BL_B = int(input('What is the bottom left value of matrix b?'))
    BR_B = int(input('What is the bottom right value of matrix b?'))

    B_top_row = np.array([[TL_B, TR_B]])
    B_bottom_row = np.array([[BL_B, BR_B]])
    B = np.concatenate((B_top_row, B_bottom_row), axis=0)
    print('Here is the matrix you just created')
    print('')
    print(B)
    print('')
    temp = False
    while temp != True:
        choice_2 = input('Would you like to re-assign the values of the matrix you just created Y/N?')
        if choice_2 == 'N':
            temp = True
            change = 2
        elif choice_2 == 'Y':
            temp = True
        else:
            print('Not a valid answer, try again')
