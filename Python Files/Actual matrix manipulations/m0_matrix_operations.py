print("------------------------------------------------------------------------")
print("")
print("Welcome to the menu of matrix operations, please choose an option below:")
print("""
 (1) - Add Two matrices
 (2) - Subtract two matrices
 (3) - Multiply two matrices
 (4) - Find the inverse of a matrix
 (5) - Find the eignevalues and eigenvectors of a matrix
 (6) - Diagonalise a matrix
 (7) - Raise e to the power of a matrix""")
print("")

menu_option = input("What would you like to do? ")
while menu_option != "1" and menu_option != "2" and menu_option != "3" and menu_option != "4" and menu_option != "5" and menu_option != "6" and menu_option != "7":
    print('Invalid responce')
    menu_option = input("What would you like to do? ")

if menu_option == "1":
    from m2_addition_of_matrices import *
if menu_option == "2":
    from m3_subtraction_of_matrices import *
if menu_option == "3":
    from m4_multiplying_matrices import *
if menu_option == "4":
    from m5_inverse_of_a_matrix import *
if menu_option == "5":
    from m6_calculating_eigenvalues_and_eigenvectors import *
if menu_option == "6":
    from m7_diagonalisation import * 
if menu_option == "7":
    from m8_e_power_matrix import *
