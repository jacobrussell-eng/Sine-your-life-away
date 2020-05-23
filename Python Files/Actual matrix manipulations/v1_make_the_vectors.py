import numpy as np


def create_one_vector():
    change = 0
    temp = False
    while change != 1:
    
        v1 = np.array([])
        
        dimensions = int(input("How many components do the vectors consist of? "))

        for i in range (0, dimensions):
            v_component = float(input("Please enter component " + str(i+1) + " of the vector "))
            v1 =  np.append(v1, v_component)
        v1_visuals = np.array([v1])
        v1_visuals = v1_visuals.T
        print('')
        print(v1_visuals)
        print("")
        temp = False
        while temp != True:
            choice_1 = input('Would you like to re-assign the values of the vector you just created Y/N?')
            if choice_1 == 'N':
                temp = True
                change = 1
            elif choice_1 == 'Y':
                temp = True
            else:
                print('Not a valid answer, try again')
    return(v1)
    
def create_two_vectors():
    change = 0
    temp = False
    while change != 1:

        v1 = np.array([])
        v2 = np.array([])

        dimensions = int(input("How many components do the vectors consist of? "))

        for i in range (0, dimensions):
            v_component = float(input("Please enter component " + str(i+1) + " of the first vector "))
            v1 =  np.append(v1, v_component)
        v1_visuals = np.array([v1])
        v1_visuals = v1_visuals.T
        print("")

        for i in range (0, dimensions):
            v_component = float(input("Please enter component " + str(i+1) + " of the second vector "))
            v2 =  np.append(v2, v_component)
        v2_visuals = np.array([v2])
        v2_visuals = v2_visuals.T
        print('')
        print(v1_visuals)
        print('')
        print(v2_visuals)
        print("")
        temp = False
        while temp != True:
            choice_1 = input('Would you like to re-assign the values of the vectors you just created Y/N?')
            if choice_1 == 'N':
                temp = True
                change = 1
            elif choice_1 == 'Y':
                temp = True
            else:
                print('Not a valid answer, try again')

    return (v1, v2)






