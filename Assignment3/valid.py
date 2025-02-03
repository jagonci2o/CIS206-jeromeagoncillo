try:
    #1 Data type validation that makes sure the user enters a valid whole number
    number = int(input("Please enter a whole number between 1-30: "))

    #1 Range and constraint validation that checks if the number is within
    # the range given
    if number > 30:
        print(f"{number} is greater than 30 and not in range.")
    elif number < 1:
        print(f"{number} is less than 1 and not in range.")
    else:
        print(f"You entered: {number}")

        #3 Nested if statement that first figures out if number is even
        # then if it is a multiple of 9
        if number % 2 == 0:
            print(f"{number} is even.")
            if number % 8 == 0:  # Checks if number is a multiple of 8
                print(f"{number} is also a multiple of 8!")
        else:
            print(f"{number} is odd.")

#2 Value error handles exceptions when invalid input. This case, a
# non-integer whole numeber
except ValueError:
    print(f"Invalid input. {number} is not a valid whole number.")
