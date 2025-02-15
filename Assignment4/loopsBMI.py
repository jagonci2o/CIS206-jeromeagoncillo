print("\nHello! I will ask you to enter your weight in pounds and height in feet and inches.")
print("I will use the following information to calculate your BMI.")
print("You can quit at any time by entering the letter, \"q\", case insensitive ")

# Will ask the user for their weight (lbs) and height (ft and in)
def userWeightAndHeight():
    while True: 
        try:
            weight = input("\nPlease enter your weight (lbs): ")
            if weight == 'Q' or weight == 'q':
                exit()
            else:
                floWeight = float(weight)
            break
        except ValueError:
            print("Invalid input. Please try again.")
    
    while True:
        try:    
            heightFt = input("\nPlease enter your height (ft): ")
            if heightFt == 'Q' or heightFt == 'q':
                exit()
            else:
                floHeightFt = float(heightFt)
            break 
        except ValueError:
            print("Invalid input. Please try again.")
    
    while True:
        try:
            heightIn = input("\nPlease enter your height (in): ")
            if heightIn == 'Q' or heightIn == 'q':
                exit()
            else:
                floHeightIn = float(heightIn)
            break
        except ValueError:
            print("Invalid input. Please try again.")
    
    floHeightTotal = (floHeightFt * 12) + floHeightIn 
    return floWeight, floHeightTotal

# Grabs the users weight and height, and calculates BMI
def calculateBMI(pounds, inches):
    BMI = ( pounds / ( inches * inches ) ) * 703
    return BMI

# Displays a legend of 3 BMI ranges: Underweight, Normal, and Overweight
# Also displays the BMI Table 
def displayRange():
    print("\nUnderweight: < 18.4")
    print("Normal: 18.5-24.9")
    print("Overweight: 25.0-29.9")

    print("\nThe BMI table:")
    print(end= "    ")
    
    # For loop that prints columns for height from 58 inches to 76 inches 
    # in 2-inch increments
    for labelHeights in range(58, 76, 2):
        print(f"{labelHeights:>5}", end = " ")
    
    print()
    # For loop that prints rows for weight from 100 lbs to 250 lbs in
    # 10-lbs increments
    for labelWeights in range(100, 250, 10):
        print(f"{labelWeights:>5}", end = " ")
        # Nested for loop to print the BMI of each weight-height ratio
        for labelHeights in range(58, 76, 2):
            BMI = calculateBMI(labelWeights, labelHeights)
            print(f"{round(BMI, 1):>5}", end=" ")
        print()



userInput = 'c'
while userInput != 'q':
    floWeight, floHeightTotal = userWeightAndHeight() # tuple to get weight and height
    BMI = calculateBMI(floWeight, floHeightTotal) # Call by assignment is used to pass the local variables
    print("\nBMI:", round(BMI, 1)) # Displays the user's BMI
    displayRange() # Displays legend and BMI Table
    while True: # While loop that lets you continue calculating BMI or quit
        userInput = input("Would you like to continue (c) or quit (q): ").lower()
        if userInput == 'c' or userInput == 'q': # If-else statement to check if input is valid
            break
        else:
            print("Please enter a valid input.")
