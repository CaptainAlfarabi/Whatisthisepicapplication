import time
import random

print("\n")
print("Welcome to this epic 'program'! I made this to use my progress so far and practice. I don't know how long I'll "
      "be working on this for but it's really fun so far. \n10/31/2023  \n \n")

time.sleep(0.5)

while True:
    Username = input("Please select one of the following usernames: Red, Gary, Blue, Ash \n")

    if Username in ["Red", "Gary", "Blue", "Ash"]:
        print("You have selected the username " + Username + ".")
        break
    else:
        print("Invalid username. Please select one of the provided usernames. [Case and character sensitive]")

time.sleep(0.5)

print("Hello " + Username + "!")

time.sleep(0.5)

while True:
    Tool_selection = input("What would you like to do? Select number or type out the phrase. \n" "1.) Make a "
                           "countdown \n" "2.) Select a random number \n" "3.) Add numbers \n")

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

    elif Tool_selection.lower() == "add numbers" or Tool_selection == "3":
        while True:
            Number_Addition_Selection = input("Type the numbers you would like to add in the following format: a b c. "
                                              "This will result to the numbers being added as a + b + c. \n")
            try:
                numbers = [float(num) for num in Number_Addition_Selection.split()]
                result = sum(numbers)
                print(f"The sum of the numbers provided is {result}")
                break
            except ValueError:
                print("Invalid input. Please use correct formatting. \n")

    else:
        print("Please select an option.")
