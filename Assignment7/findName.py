def checkFile(fileCheck, name):
    with open(fileCheck, 'r') as file:
        names = [line.strip().lower() for line in file]  # Convert all names to lowercase
        
    return name.lower() in names  # Convert input name to lowercase before checking

def addToNoFound(fileNotFound, name):
    with open(fileNotFound, 'a') as file:
        file.write(name + '\n')  # Write the name to the file with a newline

def main():
    userInput = ''
    while userInput.lower() != 'q':
        userInput = input("Hello! Enter a name and I will check if it is in the names.txt file (Enter 'q' to exit): ")
        
        # Check if the user wants to quit
        if userInput.lower() == 'q':
            break
        
        # Check if the name exists in names.txt
        if checkFile('names.txt', userInput):
            print(f"The name '{userInput}' is in names.txt file.")
        else:
            print(f"The name '{userInput}' is not in names.txt file. It will be added to nofound.txt file.")
            addToNoFound('nofound.txt', userInput)

if __name__ == "__main__":
    main()
