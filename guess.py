# (1) Generate a random number from 1-100

import random
number = random.randint(1, 100)

# (2) Print the number (for easier debugging)

print("The randomly selected number is: " + str(number) + ".")

# (3) Ask the user to guess the number

user_guess = input("Hello! I've chosen a number from 1 to 100. Please guess what it is: ")
# (4) Print that the guess was too high / too low / just right!

if int(user_guess) == number:
    print("That's right! " + user_guess + " is exactly the right number!")
elif int(user_guess) < number:
    print("Sorry. My number was " + str(number) + ". " + str(user_guess) + " is too low.")
else:
    print("Sorry. My number was " + str(number) + ". " + str(user_guess) + " is too high.")
