print("------------------------------------------------------------------------")
print("\n Welcome to the menu of linear algebra, please choose an option below:")
print("""\n(1) - matrix operations
(2) - vector operations
(3) - solving simultaneous equations\n""")

selection = input("What would you like to do? ")
while selection != "1" and selection != "2" and selection != "3":
    print('Invalid response')
    selection = input("What would you like to do? ")

if selection == "1":
    from m0_matrix_operations import *
elif selection == "2":
    from v0_vector_operations import *
elif selection == "3":
    from s0_solving_sim_equations import *
