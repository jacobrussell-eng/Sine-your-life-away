import numpy as np
from m1_create_the_matrices import *

top_left_A = (A.item((0, 0)))
top_right_A = (A.item((0, 1)))
bottom_left_A = (A.item((1, 0)))
bottom_right_A = (A.item((1, 1)))

top_left_B = (B.item((0, 0)))
top_right_B = (B.item((0, 1)))
bottom_left_B = (B.item((1, 0)))
bottom_right_B = (B.item((1, 1)))


new_top_left = (top_left_A * top_left_B) + (top_right_A * bottom_left_B)
new_top_right = (top_left_A * top_right_B) + (top_right_A * bottom_right_B)
new_bottom_left = (bottom_left_A * top_left_B) + (bottom_right_A * bottom_left_B)
new_bottom_right = (bottom_left_A * top_right_B) + (bottom_right_A * bottom_right_B)


X = np.array([[new_top_left, new_top_right]])
Y = np.array([[new_bottom_left, new_bottom_right]])
Z = np.concatenate((X, Y), axis=0)
print('This is matrix a: ')
print('')
print(A)
print('')
print('This is matrix b: ')
print('')
print(B)
print('')
print('This is the resultant matrix from multiplying the two former: ')
print('')
print(Z)
 


