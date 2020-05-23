#Sid and Adam                      ---Integration & Diffrentiation---

import sys
import time

def integration():
    valid = False
    while valid == False:
        coef = input("Enter the co-efficent of your value")
        while coef.isdigit == False:
            print("Input must be an integer")
        pwr = input("Enter the power of your value")
        while pwr.isdigit == False:
            print("Input must be an integer")
        coef = int(coef)
        pwr = int(pwr)
        while 1 != 2:
            choice_b = input("Confirm that your input is " + str(coef) + "x^" + str(pwr) + " by entering [Y/N]")
            choice_b = choice_b.title()
            if choice_b == "Y":
                print("Confirmed")
                valid = True
                break
            elif choice_b == "N":
                print("OK - Change your choice...")
                break
            else:
                print("Invalid Input")
                
    print("Integrating...")
    time.sleep(2)
    print("Integrated")
    pwr_b = pwr + 1
    if int(coef/pwr_b) == float(coef/pwr_b):
        coef_b = coef/pwr_b
        print(str(coef) + "x^" + str(pwr) + " when integrated is equal to " + str(coef_b) + "x^" + str(pwr_b))
    else:
        coef = str(coef)
        pwr_b = str(pwr_b)
        print(str(coef) + "x^" + str(pwr) + " when integrated is equal to (" + coef + "x^" + pwr_b + ")/" + pwr_b)
    print("")
    time.sleep(2)    
    
def differentiate():
    run = False
    print("Welcome to 'The Diffrenciation Function'")
    print("This program can Diffrenciate any single value that you choose to submit")
    choice = input("Press Enter to run program, or X to close prgoram")
    choice = choice.title()
    while choice != "" and choice != "X":
        print("Invalid Input")
        choice = input("Press Enter to run program, or X to close prgoram")
        choice = choice.title()
    if choice == "X":
        print("You have choosen to exit")
        sys.exit()
    else:
        run = True

    print("")
    while run == True:
        valid = False
        while valid == False:
            coef = input("Enter the co-efficent of your value")
            while coef.isdigit == False:
                print("Input must be an integer")
            pwr = input("Enter the power of your value")
            while pwr.isdigit == False:
                print("Input must be an integer")
            coef = int(coef)
            pwr = int(pwr)
            while 1 != 2:
                choice_b = input("Confirm that your input is " + str(coef) + "x^" + str(pwr) + " by entering [Y/N]")
                choice_b = choice_b.title()
                if choice_b == "Y":
                    print("Confirmed")
                    valid = True
                    break
                elif choice_b == "N":
                    print("OK - Change your choice...")
                    break
                else:
                    print("Invalid Input")                  
        print("Diffrenciating...")
        pwr_b = pwr - 1
        coef_b = coef * pwr
        
        print("Diffrenciated")
        print("")
        print(str(coef) + "x^" + str(pwr) + " when diffrenciated is equal to " + str(coef_b) + "x^" + str(pwr_b))
        time.sleep(2)

print("Welcome to 'The Integration Program'")
print("This program can Integrate or Differentiate any single value that you choose to submit")
choice = input("Press '1' to Integrate, '2' to Differentiate, or X to close the prgoram")
choice = choice.title()
while choice != "1"  and choice != "2" and choice != "X":
    print("Invalid Input")
    choice = input("Press Enter to run program, or X to close prgoram")
    choice = choice.title()
if choice == "X":
    print("You have choosen to exit")
    sys.exit()
elif choice == "1":
    print("You have choosen to Integrate")
    print("")
    integration()
else:
    print("You have choosen to Differentiate")
    print("")
    differentiate()
    
