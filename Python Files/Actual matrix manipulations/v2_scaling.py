import numpy as np
from v1_make_the_vectors import create_one_vector
v1 = create_one_vector()




scaler = float(input("What would you like to scale your vector by? "))

def scaling(v1):
    for i in range(len(v1)):
        v1[i] = scaler * v1[i]
    vector = np.array([v1])
    vector = vector.T
    print('You get the following vector: ')
    print('')    
    print(vector)

scaling(v1)
    
    
