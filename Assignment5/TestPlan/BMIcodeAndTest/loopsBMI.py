# Modified loopsBMI. Improved userWeightAndHeight to have parameters.

print("\nHello! I will ask you to enter your weight in pounds and height in feet and inches.")
print("I will use the following information to calculate your BMI.")
print("You can quit at any time by entering the letter, \"q\", case insensitive ")

# Will ask the user for their weight (lbs) and height (ft and in)
def userWeightAndHeight(weight=None, heightFt=None, heightIn=None):
    if weight is None:
        while True:
            try:
                weight = input("\nPlease enter your weight (lbs): ")
                if weight.lower() == 'q':
                    exit()
                floWeight = float(weight)
                if floWeight <= 0:
                    print("Weight must be a positive number. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please try again.")
    else:
        floWeight = float(weight)
        if floWeight <= 0:
            raise ValueError("Weight must be a positive number.")

    if heightFt is None:
        while True:
            try:    
                heightFt = input("\nPlease enter your height (ft): ")
                if heightFt.lower() == 'q':
                    exit()
                floHeightFt = float(heightFt)
                if floHeightFt < 0:
                    print("Height in feet cannot be negative. Please try again.")
                    continue
                break 
            except ValueError:
                print("Invalid input. Please try again.")
    else:
        floHeightFt = float(heightFt)
        if floHeightFt < 0:
            raise ValueError("Height in feet cannot be negative.")

    if heightIn is None:
        while True:
            try:
                heightIn = input("\nPlease enter your height (in): ")
                if heightIn.lower() == 'q':
                    exit()
                floHeightIn = float(heightIn)
                if floHeightIn < 0:
                    print("Height in inches cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please try again.")
    else:
        floHeightIn = float(heightIn)
        if floHeightIn < 0:
            raise ValueError("Height in inches cannot be negative.")

    floHeightTotal = (floHeightFt * 12) + floHeightIn
    if floHeightTotal <= 0:
        raise ValueError("Total height must be greater than zero.")

    return floWeight, floHeightTotal

# Grabs the users weight and height, and calculates BMI
def calculateBMI(pounds, inches):
    if inches <= 0:
        raise ValueError("Height must be a positive number.")
    return (pounds / (inches * inches)) * 703


# Displays a legend of 3 BMI ranges: Underweight, Normal, and Overweight
# Also displays the BMI Table 
def displayRange():
    print("\nUnderweight: < 18.4")
    print("Normal: 18.5-24.9")
    print("Overweight: 25.0-29.9")

    print("\nThe BMI table:")
    print(end="    ")
    
    # For loop that prints columns for height from 58 inches to 76 inches 
    # in 2-inch increments
    for labelHeights in range(58, 76, 2):
        print(f"{labelHeights:>5}", end=" ")
    
    print()
    # For loop that prints rows for weight from 100 lbs to 250 lbs in
    # 10-lbs increments
    for labelWeights in range(100, 250, 10):
        print(f"{labelWeights:>5}", end=" ")
        for labelHeights in range(58, 76, 2):
            # Nested for loop to print the BMI of each weight-height ratio
            BMI = calculateBMI(labelWeights, labelHeights)
            print(f"{round(BMI, 1):>5}", end=" ")
        print()

def main():
    userInput = 'c'
    while userInput != 'q':
        floWeight, floHeightTotal = userWeightAndHeight() # tuple to get weight and height
        BMI = calculateBMI(floWeight, floHeightTotal) # Call by assignment is used to pass the local variables
        print("\nBMI:", round(BMI, 1)) # Displays the user's BMI
        displayRange() # Displays legend and BMI Table
        
        # While loop that lets you continue calculating BMI or quit
        while True:
            userInput = input("\nWould you like to continue (c) or quit (q): ").lower()
            # If-else statement to check if input is valid
            if userInput == 'c' or userInput == 'q':
                break
            else:
                print("Please enter a valid input.")

if __name__ == "__main__":
    main()
