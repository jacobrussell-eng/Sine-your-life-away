print("------------------------------------------------------------------------")
print("")
print("Welcome to the menu of linear algebra, please choose an option below:")
print("")
print("""
 (1) - matrix operations
 (2) - vector operations
 (3) - solving similtaneous equations""")
print("")

selection = input("What would you like to do? ")
while selection != "1" and selection != "2" and selection != "3":
    print('Invalid responce')
    selection = input("What would you like to do? ")

if selection == "1":
    from m0_matrix_operations import *
elif selection == "2":
    from v0_vector_operations import *
elif selection == "3":
    from s0_solving_sim_equations import *
