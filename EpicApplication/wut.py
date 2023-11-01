import time
import random

print("\n")

while True:
    Show_Description_And_Logs = input("Would you like to see the program description and logs? Yes/No \n")
    if Show_Description_And_Logs.lower() == "yes":
        print("\n Welcome to this epic 'program'! I made this to use my progress so far and practice. I don't know how "
              "long I'll be working on this for but it's really fun so far. \n10/31/2023  \n \n")
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
        print("You have selected the username " + Username + ".")
        break
    else:
        print("Invalid username. Please select one of the provided usernames. [Case and character sensitive]")

time.sleep(0.5)

print("Hello " + Username + "!")

time.sleep(0.5)

while True:
    Tool_selection = input("What would you like to do? Select number or type out the phrase. \n" "1.) Make a "
                           "countdown \n" "2.) Select a random number \n" "3.) Add numbers \n" "4.) Multiply 2 "
                           "numbers \n" "5.) Divide 2 numbers \n")

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

    elif Tool_selection.lower() == "multiply 2 numbers" or Tool_selection == "4":
        while True:
            try:
                Multiplication_Number_Selection_1 = int(input("Type one number you would like to multiply. \n"))
                Multiplication_Number_Selection_2 = int(input("Type what you would like to multiple that number by.\n"))
                Result = Multiplication_Number_Selection_1 * Multiplication_Number_Selection_2
                print("Your result is " + str(Result) + ".")
                break
            except ValueError as e:
                print(e)
                print("Invalid input. Please enter valid integers.")
            except Exception as e:
                print(e)
                print("Something went wrong! Did you input your values correctly?")

    elif Tool_selection.lower() == "divide 2 numbers" or Tool_selection.lower() == "5":
        while True:
            try:
                Division_Number_Selection_1 = int(input("Type one number you would like to divide. \n"))
                Division_Number_Selection_2 = int(input("Type the number you would like to divide selected number by. "
                                                        "\n"))
                Result = Division_Number_Selection_1 / Division_Number_Selection_2
                print("Your result is " + str(Result) + ".")
                break
            except ValueError as e:
                print(e)
                print("Invalid input. Please enter valid integers.")
            except Exception as e:
                print(e)
                print("Something went wrong! Did you input your values correctly?")

    else:
        print("Please select an option.")
