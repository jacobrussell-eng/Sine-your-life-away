print("------------------------------------------------------------------------")
print("")
print("Welcome to the menu of solving similtaneous equations, please choose an option below:")
print("")
print("""
 (1) - two equations [using matrices]
 (2) - three equations [using guassian elimination]""")
print("")
selection = input("What would you like to do? ")
while selection != "1" and selection != "2":
    print('Invalid responce')
    selection = input("What would you like to do? ")

if selection == "1":
    from s2_system_of_equations import *
elif selection == "2":
    from s3_guassian_elim import *


