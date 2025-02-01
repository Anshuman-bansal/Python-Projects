# Dice Roller Simulation
# Description: This script simulates rolling two dice and allows the user 
#              to roll again until they choose to stop.

import random
import time

user_choice = "YES"

while user_choice == "YES" or  user_choice == "Y":

    print("Dice spinning ...")
    time.sleep(1)
    
    rolling_number_1 = random.randint(1,6)
    rolling_number_2 = random.randint(1,6)
    
    print("\nDice-1 value is : ",rolling_number_1,"\nDice-2 value is : ",rolling_number_2,"\n")    

    time.sleep(1)

    if rolling_number_2 == rolling_number_1:
        print("Congrats! You got the same values.\n")

    user_choice = input("Do you want to roll the dice again? (y/n)  --> ").upper()

print("Thank you for generating random dice numbers!")
