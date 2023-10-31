import time
import random

print("Welcome to this epic program! I made this on my free time and might continue updating for a while. \n \n")

time.sleep(0.5)

while True:
    Username = input("Please select one of the following usernames: Red, Gary, Blue, Ash \n")

    if Username in ["Red", "Gary", "Blue", "Ash"]:
        print("You have selected the username " + Username + ".")
        break
    else:
        print("Invalid username. Please select one of the provided usernames.")

time.sleep(0.5)

print("Hello " + Username + "!")

time.sleep(0.5)

while True:
    Tool_selection = input("What would you like to do? Select number or type out the phrase. \n" "1.) Make a "
                           "countdown \n" "2.) Select a random number \n")

    if Tool_selection.lower() == "make a countdown" or Tool_selection == "1":
        while True:
            Countdown_Time_Selection = input("Select the amount of seconds for the countdown: \n")
            if Countdown_Time_Selection.isdigit():
                Countdown_Time_Selection = int(Countdown_Time_Selection)
                for i in range(Countdown_Time_Selection, 0, -1):
                    print(i)
                    time.sleep(1)
                break
            else:
                print("Invalid selection. Please choose an integer.")

    elif Tool_selection.lower() == "select a random number" or Tool_selection == "2":
        while True:
            Random_Number_Selection = input("Do you want to roll a dice (type 'Dice') or specify a custom range? ("
                                            "e.g., '1 10')\n")
            if Random_Number_Selection.lower() == "dice":
                random_number = random.randint(1, 6)
                print(f"Random number: {random_number}")
                break
            else:
                try:
                    min_range, max_range = map(int, Random_Number_Selection.split())
                    if min_range <= max_range:
                        random_number = random.randint(min_range, max_range)
                        print(f"Random number: {random_number}")
                        break
                    else:
                        print("Invalid range. The first number should be less than or equal to the second number.")
                except ValueError:
                    print("Invalid input. Please enter two numbers or 'Dice'.")

    else:
        print("Please select an option.")
