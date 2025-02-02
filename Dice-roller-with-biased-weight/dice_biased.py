# Biased Dice Roller Simulation
# Description: This script simulates rolling two biased dice, 
#              favoring certain numbers more than others.

import random
import time

#  (Modify these to adjust bias)
biased_numbers = [1, 2, 3, 4, 5, 6]
weights = [5, 10, 15, 40, 20, 10]  # Higher weight = Higher probability

user_choice = "YES"

while user_choice == "YES" or user_choice == "Y":

    print("Dice spinning ...")
    time.sleep(1)
    
    # Generate biased rolls
    rolling_number_1 = random.choices(biased_numbers, weights=weights, k=1)[0]
    rolling_number_2 = random.choices(biased_numbers, weights=weights, k=1)[0]

    print("\nDice-1 value is : ", rolling_number_1, "\nDice-2 value is : ", rolling_number_2, "\n")    

    time.sleep(1)

    if rolling_number_2 == rolling_number_1:
        print("Congrats! You got the same values.\n")

    user_choice = input("Do you want to roll the dice again? (y/n)  --> ").upper()

print("Thank you for generating biased dice numbers!")
