import time
import random

print("\n")

print("----------------------------------------")
print(" WELCOME TO EPIC APPLICATION VERSION 1.0")
print("----------------------------------------")


while True:
    Show_Description_And_Logs = input("Would you like to see the program description and logs? Yes/No \n")
    if Show_Description_And_Logs.lower() == "yes":
        print("\n Welcome to this epic 'program'! I made this to use my progress so far and practice. I don't know how "
              "long I'll be working on this for but it's really fun so far. \n10/31/2023  \nI added my first game! "
              "Rock paper scissors is now available via. option 6.\n11/3/2023\n\n")
        break
    elif Show_Description_And_Logs.lower() == "no":
        print("\n")
        break
    else:
        print("Invalid selection. Please type out 'yes' or 'no'")

time.sleep(0.5)

while True:
    Username = input("Please select one of the following usernames: Red, Gary, Blue, Ash \n")

    if Username in ["Red", "Gary", "Blue", "Ash"]:
        time.sleep(0.5)
        print("You have selected the username " + Username + ".\n")
        break
    else:
        time.sleep(0.5)
        print("Invalid username. Please select one of the provided usernames. [Case and character sensitive]\n")

time.sleep(0.5)

print("Hello " + Username + "!\n")

time.sleep(0.5)

while True:
    Tool_selection = input("What would you like to do? Select number or type out the phrase. \n" "1.) Make a "
                           "countdown \n" "2.) Select a random number \n" "3.) Add numbers \n" "4.) Multiply 2 "
                           "numbers \n" "5.) Divide 2 numbers \n" "6.) Play Rock Paper Scissors against Computer \n")

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
                time.sleep(0.5)
                print("Invalid selection. Please choose an integer.")

    elif Tool_selection.lower() == "select a random number" or Tool_selection == "2":
        while True:
            Random_Number_Selection = input("Do you want to roll a dice (type 'Dice') or specify a custom range? ("
                                            "e.g., '1 10')\n")
            if Random_Number_Selection.lower() == "dice":
                random_number = random.randint(1, 6)
                time.sleep(0.5)
                print(f"Random number: {random_number}\n")
                break
            else:
                try:
                    min_range, max_range = map(int, Random_Number_Selection.split())
                    if min_range <= max_range:
                        random_number = random.randint(min_range, max_range)
                        time.sleep(0.5)
                        print(f"Random number: {random_number}\n")
                        break
                    else:
                        time.sleep(0.5)
                        print("Invalid range. The first number should be less than or equal to the second number.")
                except ValueError:
                    time.sleep(0.5)
                    print("Invalid input. Please enter two numbers or 'Dice'.")

    elif Tool_selection.lower() == "add numbers" or Tool_selection == "3":
        while True:
            Number_Addition_Selection = input("Type the numbers you would like to add in the following format: a b c. "
                                              "This will result to the numbers being added as a + b + c. \n")
            try:
                numbers = [float(num) for num in Number_Addition_Selection.split()]
                result = sum(numbers)
                time.sleep(0.5)
                print(f"The sum of the numbers provided is {result}\n")
                break
            except ValueError:
                time.sleep(0.5)
                print("Invalid input. Please use correct formatting. \n")

    elif Tool_selection.lower() == "multiply 2 numbers" or Tool_selection == "4":
        while True:
            try:
                Multiplication_Number_Selection_1 = int(input("Type one number you would like to multiply. \n"))
                Multiplication_Number_Selection_2 = int(input("Type what you would like to multiple that number by.\n"))
                Result = Multiplication_Number_Selection_1 * Multiplication_Number_Selection_2
                time.sleep(0.5)
                print("Your result is " + str(Result) + ".\n")
                break
            except ValueError as e:
                time.sleep(0.5)
                print(e)
                print("Invalid input. Please enter valid integers.\n")
            except Exception as e:
                time.sleep(0.5)
                print(e)
                print("Something went wrong! Did you input your values correctly?\n")

    elif Tool_selection.lower() == "divide 2 numbers" or Tool_selection == "5":
        while True:
            try:
                Division_Number_Selection_1 = int(input("Type one number you would like to divide. \n"))
                Division_Number_Selection_2 = int(input("Type the number you would like to divide selected number by. "
                                                        "\n"))
                Result = Division_Number_Selection_1 / Division_Number_Selection_2
                time.sleep(0.5)
                print("Your result is " + str(Result) + ".\n")
                break
            except ValueError as e:
                time.sleep(0.5)
                print(e)
                print("Invalid input. Please enter valid integers.\n")
            except Exception as e:
                time.sleep(0.5)
                print(e)
                print("Something went wrong! Did you input your values correctly?\n")

    elif Tool_selection.lower() == "play rock paper scissors against computer" or Tool_selection == "6":
        print("Input your selection of rock, paper, or scissors. The computer will instantaneously select an option.\n")
        while True:
            choices = ["rock", "paper", "scissors"]
            computer = random.choice(choices)
            player = None
            while player not in choices:
                player = input("Select rock, paper, or scissors.\n").lower()
            if player == computer:
                time.sleep(0.5)
                print("Computer chose: " + computer + "\n" "You chose: " + player + "\n")
                time.sleep(0.5)
                print("Tie Game.\n")
            elif player == "rock":
                if computer == "paper":
                    time.sleep(0.5)
                    print("Computer chose: " + computer + "\n" "You chose: " + player + "\n")
                    time.sleep(0.5)
                    print("You lost. \n")
                if computer == "scissors":
                    time.sleep(0.5)
                    print("Computer chose: " + computer + "\n" "You chose: " + player + "\n")
                    time.sleep(0.5)
                    print("You won. \n")
            elif player == "paper":
                if computer == "scissors":
                    time.sleep(0.5)
                    print("Computer chose: " + computer + "\n" "You chose: " + player + "\n")
                    time.sleep(0.5)
                    print("You lost. \n")
                if computer == "rock":
                    time.sleep(0.5)
                    print("Computer chose: " + computer + "\n" "You chose: " + player + "\n")
                    time.sleep(0.5)
                    print("You won. \n")
            elif player == "scissors":
                if computer == "rock":
                    time.sleep(0.5)
                    print("Computer chose: " + computer + "\n" "You chose: " + player + "\n")
                    time.sleep(0.5)
                    print("You lost. \n")
                if computer == "paper":
                    time.sleep(0.5)
                    print("Computer chose: " + computer + "\n" "You chose: " + player + "\n")
                    time.sleep(0.5)
                    print("You won. \n")
            play_rps_again = input("Would you like to play Rock Paper Scissors again?(Yes/No)\n")
            if play_rps_again.lower() == "no":
                print("\n")
                break
            elif play_rps_again.lower() != "yes":
                print("Invalid option.\n")
                break

    else:
        print("Please select an option.")
