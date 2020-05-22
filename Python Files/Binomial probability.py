#Sidharth                        20th December 2018

import math
import time

def combinations():
    valid = False
    while valid == False:
        n = input("Enter the number of objects in the set")
        while n.isdigit == False:
            print("Input must be an integer")
        r = input("Enter the amount of objects taken from this set")
        while r.isdigit == False:
            print("Input must be an integer")
        n = int(n)
        r = int(r)
        while 1 != 2:
            choice_b = input("Confirm that your input is: " + str(n) + "C" + str(r) + " by entering [Y/N]")
            choice_b = choice_b.title()
            if choice_b == "Y":
                print("Confirmed")
                print("")
                valid = True
                break
            elif choice_b == "N":
                print("OK - Change your choice...")
                break
            else:
                print("Invalid Input")
                
    print("Caculating the binomial probability...")
    time.sleep(2)
    print("Calculated")
    print("")
    ans = math.factorial(n) / (math.factorial(r) * (math.factorial(n-r)))
    print(str(n) + "C" + str(r),  "equals " + str(ans))
    
    print("")
    time.sleep(2)



def permutations():
    valid = False
    while valid == False:
        n = input("Enter the number of objects in the set")
        while n.isdigit == False:
            print("Input must be an integer")
        r = input("Enter the amount of objects taken from this set")
        while r.isdigit == False:
            print("Input must be an integer")
        n = int(n)
        r = int(r)
        while 1 != 2:
            choice_b = input("Confirm that your input is: " + str(n) + "P" + str(r) + " by entering [Y/N]")
            choice_b = choice_b.title()
            if choice_b == "Y":
                print("Confirmed")
                print("")
                valid = True
                break
            elif choice_b == "N":
                print("OK - Change your choice...")
                break
            else:
                print("Invalid Input")
                
    print("Caculating the binomial probability...")
    time.sleep(2)
    print("Calculated")
    print("")
    ans = math.factorial(n) /(math.factorial(n-r))
    print(str(n) + "P" + str(r),  "equals " + str(ans))
    
    print("")
    time.sleep(2)

print("Welcome to 'The Permutation/Combination Program'")
print("This program can calculate the amount of permutations/combinations in which a ceratin event can occur")
choice = input("Press '1' to calculate the amount of permutations, '2' to calculate the amount of combinations, or X to close the prgoram")
choice = choice.title()
while choice != "1"  and choice != "2" and choice != "X":
    print("Invalid Input")
    choice = input("Press Enter to run program, or X to close prgoram")
    choice = choice.title()
if choice == "X":
    print("You have choosen to exit")
    sys.exit()
elif choice == "1":
    print("You have choosen to calculate the amount of permutations")
    print("")
    permutations()
else:
    print("You have choosen to calculate the amount of combinations")
    print("")
    combinations()
