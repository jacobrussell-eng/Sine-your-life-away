from m7_diagonalisation import *

#Matrix e^D
e_D = np.array([[np.exp(eig_val_1), 0], [0, np.exp(eig_val_2)]])

#Matrix e^A
e_A = (P.dot(e_D.dot(P_inverse)))

print('e ^ A is equal to: ')
print('')
print(e_A)