import numpy as np
from v1_make_the_vectors import create_two_vectors
array = create_two_vectors()
v1 = array[0]
v2 = array[1]

def dot_product(v1, v2):
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    print('The dot product gives: ')
    print('')
    print(total)

    
dot_product(v1, v2)
