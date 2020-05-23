import numpy as np
temp = False
change = 0
while change != 1:
    #Equation one co-efficiants

    x_1 = int(input('What is the coefficiant of x in the first equation? '))
    y_1 = int(input('What is the coefficiant of y in the first equation? '))
    z_1 = int(input('What is the coefficiant of z in the first equation? '))
    RHS_1 = int(input('What does the first equation equal? '))
    print('')

    #Equation two co-efficiants

    x_2 = int(input('What is the coefficiant of x in the second equation? '))
    y_2 = int(input('What is the coefficiant of y in the second equation? '))
    z_2 = int(input('What is the coefficiant of z in the second equation? '))
    RHS_2 = int(input('What does the second equation equal? '))
    print('')

    #Equation three co-efficiants

    x_3 = int(input('What is the coefficiant of x in the third equation? '))
    y_3 = int(input('What is the coefficiant of y in the third equation? '))
    z_3 = int(input('What is the coefficiant of z in the third equation? '))
    RHS_3 = int(input('What does the third equation equal? '))
    
    

    


    #Computing rows
    Table_top_row = np.array([[x_1, y_1, z_1, RHS_1]])
    Table_middle_row = np.array([[x_2, y_2, z_2, RHS_2]])
    Table_bottom_row = np.array([[x_3, y_3, z_3, RHS_3]])

    #Display rows
    Table_top_row_display = np.array([[x_1, y_1, z_1, '|', RHS_1]],  dtype=object)
    Table_middle_row_display = np.array([[x_2, y_2, z_2, '|', RHS_2]],  dtype=object)
    Table_bottom_row_display = np.array([[x_3, y_3, z_3, '|', RHS_3]],  dtype=object)

    #Tables
    Table_display = np.concatenate((Table_top_row_display, Table_middle_row_display, Table_bottom_row_display))
    Table = np.concatenate((Table_top_row, Table_middle_row, Table_bottom_row), axis=0)


    print('')
    print('The originL Matrix is: ')
    print('')
    print(Table_display)
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



print('')
print('Iteration one gives: ')
print('')

#Coloumn 1

#Computing rows
top_left = Table[0, 0]
Table_top_row = Table_top_row / top_left

middle_left = Table[1, 0]
Table_middle_row = (middle_left*-1)*Table_top_row + Table_middle_row

bottom_left = Table[2, 0]
Table_bottom_row = (bottom_left*-1)*Table_top_row + Table_bottom_row

#Table computing
Table = np.concatenate((Table_top_row, Table_middle_row, Table_bottom_row), axis=0)

#Display rows
Table_top_row_display = np.array([[round(Table[0, 0], 1), round(Table[0, 1], 1), round(Table[0, 2], 1), '|', round(Table[0, 3], 1)]],  dtype=object)
Table_middle_row_display = np.array([[round(Table[1, 0], 1), round(Table[1, 1], 1), round(Table[1, 2], 1), '|', round(Table[1, 3], 1)]],  dtype=object)
Table_bottom_row_display = np.array([[round(Table[2, 0], 1), round(Table[2, 1], 1), round(Table[2, 2], 1), '|', round(Table[2, 3], 1)]],  dtype=object)

#Table display
Table_display = np.concatenate((Table_top_row_display, Table_middle_row_display, Table_bottom_row_display))

print(Table_display)
print('')
print('Iteration two gives: ')
print('')

#Coloumn 2

#Computing rows
middle_middle = Table[1, 1]
Table_middle_row = Table_middle_row / middle_middle

top_middle = Table[0, 1]
Table_top_row = (top_middle*-1)*Table_middle_row + Table_top_row

bottom_middle = Table[2, 1]
Table_bottom_row = (bottom_middle*-1)*Table_middle_row + Table_bottom_row

#Table computing
Table = np.concatenate((Table_top_row, Table_middle_row, Table_bottom_row), axis=0)

#Display rows
Table_top_row_display = np.array([[round(Table[0, 0], 1), round(Table[0, 1], 1), round(Table[0, 2], 1), '|', round(Table[0, 3], 1)]],  dtype=object)
Table_middle_row_display = np.array([[round(Table[1, 0], 1), round(Table[1, 1], 1), round(Table[1, 2], 1), '|', round(Table[1, 3], 1)]],  dtype=object)
Table_bottom_row_display = np.array([[round(Table[2, 0], 1), round(Table[2, 1], 1), round(Table[2, 2], 1), '|', round(Table[2, 3], 1)]],  dtype=object)

#Table display
Table_display = np.concatenate((Table_top_row_display, Table_middle_row_display, Table_bottom_row_display))


print(Table_display)
print('')
print('Iteration three givess: ')
print('')

#Coloumn 3

#Computing rows
bottom_right = Table[2, 2]
Table_bottom_row = Table_bottom_row / bottom_right

middle_right = Table[1, 2]
Table_middle_row = (middle_right*-1)*Table_bottom_row + Table_middle_row

top_right = Table[0, 2]
Table_top_row = (top_right*-1)*Table_bottom_row + Table_top_row

#computing table
Table = np.concatenate((Table_top_row, Table_middle_row, Table_bottom_row), axis=0)

#Display rows
Table_top_row_display = np.array([[round(Table[0, 0], 1), round(Table[0, 1], 1), round(Table[0, 2], 1), '|', round(Table[0, 3], 1)]],  dtype=object)
Table_middle_row_display = np.array([[round(Table[1, 0], 1), round(Table[1, 1], 1), round(Table[1, 2], 1), '|', round(Table[1, 3], 1)]],  dtype=object)
Table_bottom_row_display = np.array([[round(Table[2, 0], 1), round(Table[2, 1], 1), round(Table[2, 2], 1), '|', round(Table[2, 3], 1)]],  dtype=object)

#Table display
Table_display = np.concatenate((Table_top_row_display, Table_middle_row_display, Table_bottom_row_display))

print(Table_display)
print('')

print('x = ', round(Table[0, 3], 5))
print('y = ', round(Table[1, 3], 5))
print('z = ', round(Table[2, 3], 5))


