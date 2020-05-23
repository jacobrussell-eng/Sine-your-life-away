import numpy as np
print('This will solve LP problems with two constraints and three variables')
print('The equations will be in the form:  P, x, y, z, s1, s2, s3')
print('')


#Objective function

p_1 = 1
x_1 = int(input('What is the coefficiant of x in the objective equation? '))
y_1 = int(input('What is the coefficiant of y in the objective equation? '))
z_1 = int(input('What is the coefficiant of z in the objective equation? '))
s1_1 = 0
s2_1 = 0
RHS_1 = 0
print('')

#Constraint 1

p_2 = 0
x_2 = int(input('What is the coefficiant of x in the first constraint? '))
y_2 = int(input('What is the coefficiant of y in the first constraint? '))
z_2 = int(input('What is the coefficiant of z in the first constraint? '))
s1_2 = 1
s2_2 = 0
RHS_2 = int(input('What does the first constraint equal? '))
print('')

#Constraint 2

p_3 = 0
x_3 = int(input('What is the coefficiant of x in the second equation? '))
y_3 = int(input('What is the coefficiant of y in the second equation? '))
z_3 = int(input('What is the coefficiant of z in the second equation? '))
s1_3 = 0
s2_3 = 1
RHS_3 = int(input('What does the second constraint equal? '))
print('')

#Making the initial table
Table_top_row = np.array([[p_1, x_1, y_1, z_1, s1_1, s2_1, RHS_1]])
Table_middle_row = np.array([[p_2, x_2, y_2, z_2, s1_2, s2_2, RHS_2]])
Table_bottom_row = np.array([[p_3, x_3, y_3, z_3, s1_3, s2_3, RHS_3]])
Table = np.concatenate((Table_top_row, Table_middle_row, Table_bottom_row), axis=0)
print('The original table is: ')
print('')
print(Table)

x = 0
while Table[0, 0] <0 or Table[0, 1] <0 or Table[0, 2] <0 or Table[0, 3] <0 or Table[0, 4] <0 or Table[0, 5] <0:
    x = x +1



    # Finding smallest value

    list = (Table[0, 0], Table[0, 1], Table[0, 2], Table[0, 3], Table[0, 4], Table[0, 5])
    smallest = (min(list))

    #finding index of smallest value
    result = np.where(Table == smallest)
    b = (result[1])
    a = int(b[0])
    print('The piviot coloumn is the coloumn', a+1, 'across')
    print('')
    print('Iteration', x)


    #Ratio 1
    ratio_1_neum = (Table[1, 6])                        
    ratio_1_denom = (Table[1, a])

    ratio_1 = ratio_1_neum / ratio_1_denom

    #Ratio 2
    ratio_2_neum = (Table[2, 6])                         
    ratio_2_denom = (Table[2, a])                         
    ratio_2 = ratio_2_neum / ratio_2_denom

    #Establishing important numbers
    top_num = Table[0, a]
    middle_num = Table[1, a]
    bottom_num = Table[2, a]

    # Selecting the correct row
    smallest_test = ratio_1 - ratio_2

    #If row 3 has the smallest ratio
    if smallest_test > 0:
        important_row = Table_bottom_row
        denom = ratio_2_denom
        new_row_three = (important_row)/denom
        Table_bottom_row  = new_row_three
        #print(Table_bottom_row)

        middle_num = middle_num * -1
        new_row_two = (middle_num*new_row_three) + Table_middle_row
        Table_middle_row = new_row_two
        #print(Table_middle_row)

        top_num = top_num * -1
        new_row_one = (top_num*new_row_three) + Table_top_row
        Table_top_row = new_row_one
        #print(Table_top_row)

        Table = np.concatenate((Table_top_row , Table_middle_row , Table_bottom_row ), axis=0)
        print(Table)


    #If row 2 has the smallest ratio
    else:
        important_row = Table_middle_row
        denom = ratio_1_denom
        new_row_two = (important_row)/denom
        Table_middle_row = new_row_two
        #print(Table_middle_row)

        bottom_num = bottom_num * -1
        new_row_three = (bottom_num*new_row_two) + Table_bottom_row
        Table_bottom_row  = new_row_three
        #print(Table_bottom_row)

        top_num = top_num * -1
        new_row_one = (top_num*new_row_two) + Table_top_row
        Table_top_row = new_row_one
        #print(Table_top_row)

        Table = np.concatenate((Table_top_row , Table_middle_row , Table_bottom_row ), axis=0)
        print(Table)
print('')

print('The optimal values are given below: ')
print('')

#x val

if (Table[0, 1] == 0 and  Table[1, 1] == 0 and  Table[2, 1] == 1):
    print('x = ', Table[2, 6])

elif (Table[0, 1] == 0 and  Table[1, 1] == 1 and  Table[2, 1] == 0):
    print('x = ', Table[1, 6])

elif (Table[0, 1] == 1 and  Table[1, 1] == 0 and  Table[2, 1] == 0):
    print('x = ', Table[0, 6])

else:
    print('x = 0')

#y val

if (Table[0, 2] == 0 and  Table[1, 2] == 0 and  Table[2, 2] == 1):
    print('y = ', Table[2, 6])

elif (Table[0, 2] == 0 and  Table[1, 2] == 1 and  Table[2, 2] == 0):
    print('y = ', Table[1, 6])

elif (Table[0, 2] == 1 and  Table[1, 2] == 0 and  Table[2, 2] == 0):
    print('y = ', Table[0, 6])

else:
    print('y = 0')

#z val

if (Table[0, 3] == 0 and  Table[1, 3] == 0 and  Table[2, 3] == 1):
    print('z = ', Table[2, 6])

elif (Table[0, 3] == 0 and  Table[1, 3] == 1 and  Table[2, 3] == 0):
    print('z = ', Table[1, 6])

elif (Table[0, 3] == 1 and  Table[1, 3] == 0 and  Table[2, 3] == 0):
    print('z = ', Table[0, 6])

else:
    print('z = 0')

#p val

if Table[0, 0] == 1:
    print('p = ', Table[0, 6])
elif Table[1, 0] == 1:
    print('p = ', Table[1, 6])
elif Table[2, 0] == 1:
    print('p = ', Table[3, 6])














