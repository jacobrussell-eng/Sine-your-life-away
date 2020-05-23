#Sid and Adam                                ---Summation---

import sys
import time

def summation():
    valid = False
    while valid == False:
        start = input("At what value is the summation begining")
        while start.isdigit == False:
            print("Input must be an integer")
        end = input("At what value is the summation ending (inclusive)")
        while end.isdigit == False:
            print("Input must be an integer")
        equation_coef = input("What is the coeficiant of the equation")
        while equation_coef.isdigit == False:
            print("Input must be an integer")
        equation_constant = input("What is the constant of the equation")
        print("")
        while equation_constant.isdigit == False:
            print("Input must be an integer")

        while 1 != 2:
            print("  " + str(end))
            print("  ∑ " + str(equation_coef) + "X + " + str(equation_constant))
            print("x = " + start)
            print("")
            choice_b = input("Is this the equation that you wanted [Y/N]")
            
                             
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
                
    print("Summing...")
    time.sleep(2)
    print("Summed")
    
    end = int(end)
    start = int(start)
    equation_coef = int(equation_coef)
    equation_constant = int(equation_constant)
    
    total = 0
    for x in range(start, end + 1):
        total = total + ((equation_coef * x) + equation_constant)

        
    total = str(total)
    print("  " + str(end))
    print("  ∑ " + str(equation_coef) + "X + " + str(equation_constant) + " = " + total)
    print("x = " + str(start))
    time.sleep(2)

summation()

