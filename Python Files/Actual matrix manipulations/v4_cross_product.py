import numpy as np


change = 0
temp = False
while change != 1:
    vec_1_i_component = float(input('What is the i component of the first vector? '))
    vec_1_j_component = float(input('What is the j component of the first vector? '))
    vec_1_k_component = float(input('What is the k component of the first vector? '))
    vec_1 = np.array([[vec_1_i_component], [vec_1_j_component], [vec_1_k_component]])
    print('')
    print(vec_1)
    print('')
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


change = 0
temp = False
while change != 1:
    vec_2_i_component = float(input('What is the i component of the second vector? '))
    vec_2_j_component = float(input('What is the j component of the second vector? '))
    vec_2_k_component = float(input('What is the k component of the second vector? '))
    vec_2 = np.array([[vec_2_i_component], [vec_2_j_component], [vec_2_k_component]])
    print('')
    print(vec_2)
    print('')
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

print('The cross product gives: ')
print('')

cross_prod_vec_i_component = (vec_1_j_component*vec_2_k_component) - (vec_1_k_component*vec_2_j_component)
cross_prod_vec_j_component = (vec_1_i_component*vec_2_k_component) - (vec_1_k_component*vec_2_i_component)
cross_prod_vec_k_component = (vec_1_i_component*vec_2_j_component) - (vec_1_j_component*vec_2_i_component)

cross_product = np.array([[cross_prod_vec_i_component], [-1*cross_prod_vec_j_component], [cross_prod_vec_k_component]])
print(cross_product)