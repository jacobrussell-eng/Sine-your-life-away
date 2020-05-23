print("------------------------------------------------------------------------")
print("")
print("Welcome to the menu of vector operations, please choose an option below:")
print("")
print("""
 (1) - scaling of a vector
 (2) - dot product of two vectors
 (3) - cross product of two vectors""")
print("")

selection = input("What would you like to do? ")
while selection != "1" and selection != "2" and selection != "3":
    print('Invalid responce')
    selection = input("What would you like to do? ")

if selection == "1":
    from v2_scaling import *
elif selection == "2":
    from v3_dot_product import *
elif selection == "3":
    from v4_cross_product import *


    
