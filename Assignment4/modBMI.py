print("Hello! I will ask you to enter your weight in pounds and height in feet and inches.")
print("I will use the following information to calculate your BMI.")
print("You can quit at any time by entering the letter, \"q\", case insensitive ")

# Will ask the user for their weight (lbs) and height (ft and in)
def userWeightAndHeight():
    while True: 
        try:
            weight = input("Please enter your weight (lbs): ")
            if weight == 'Q' or weight == 'q':
                exit()
            else:
                floWeight = float(weight)
            break
        except ValueError:
            print("Invalid input. Please try again.")
    
    while True:
        try:    
            heightFt = input("Please enter your height (ft): ")
            if heightFt == 'Q' or heightFt == 'q':
                exit()
            else:
                floHeightFt = float(heightFt)
            break 
        except ValueError:
            print("Invalid input. Please try again.")
    
    while True:
        try:
            heightIn = input("Please enter your height (in): ")
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
    
    for curheight in range(58, 76, 2):
        print(f"{curheight:>5}", end = " ")
    
    print()
    
    for curweight in range(100, 250, 10):
        print(f"{curweight:>5}", end = " ")
        for curheight in range(58, 76, 2):
            BMI = calculateBMI(curweight, curheight)
            print(f"{round(BMI, 1):>5}", end=" ")
        print()



userInput = 'c'
while userInput != 'q':
    floWeight, floHeightTotal = userWeightAndHeight() # tuple to get weight and height
    BMI = calculateBMI(floWeight, floHeightTotal) # Call by assignment is used to pass the local variables
    print("\nBMI:", f"{BMI:.1f}") # Displays the user's BMI
    displayRange() # Displays legend and BMI Table
    while True:
        userInput = input("Would you like to continue (c) or quit (q): ").lower()
        if userInput == 'c' or userInput == 'q':
            break
        else:
            print("Please enter a valid input.")
