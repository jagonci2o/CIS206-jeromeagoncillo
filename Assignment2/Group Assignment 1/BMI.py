# I worked with Adi Latic and Hatice Camalan on this assignment

print("Hello! I will ask you to enter your weight in pounds and height in feet and inches.")

# Will ask the user for their weight (lbs) and height (ft and in)
def userWeightAndHeight(): 
    weight = float(input("Please enter your weight (lbs): "))
    heightFt = float(input("Please enter your height (ft): "))
    heightIn = float(input("Please enter your height (in): "))
    heightTotal = (heightFt * 12) + heightIn # Have to convert feet to inches
    return weight, heightTotal

# Grabs the users weight and height, and calculates BMI
def calculateBMI(pounds, inches):
    
    BMI = ( pounds / ( inches * inches ) ) * 703
    print("BMI: ", f"{BMI:.1f}") # f-string to round to 1 decimal point

# Displays a legend of 3 BMI ranges: Underweight, Normal, and Overweight
def displayRange():
    print("Underweight: < 18.4")
    print("Normal: 18.5-24.9")
    print("Overweight: 25.0-29.9")


weight, heightTotal = userWeightAndHeight() # tuple to get weight and height
calculateBMI( weight, heightTotal ) # Call by assignment is used to pass the local variables
displayRange()
