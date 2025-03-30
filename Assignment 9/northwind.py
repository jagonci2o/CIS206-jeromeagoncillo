import csv 

def customersTable(filePath):
    # Load customer data from a CSV file into a list of dictionaries.
    with open(filePath, 'r') as file:  # Open the file in read mode
        return list(csv.DictReader(file))  # Read the CSV file and return a list of dictionaries

def sortCustomers(customers, attribute):
    return sorted(customers, key=lambda customer: customer[attribute])  # Return the sorted list of customers

def searchCustomers(query, customers, attribute):
    return [customer for customer in customers if query.lower() in customer[attribute].lower()]  # Return matching customers to the search

def displayCustomers(customers, order):
    # Display customer information based on a specific order
    for customer in customers:  # Check each customer in the list
        if order == 1:  # If sort by company name, display CompanyName first
            print(f"Company: {customer['companyName']}, Contact: {customer['contactName']}, Phone: {customer['phone']}")
        elif order == 2:  # If sort by contact name, display ContactName first
            print(f"Contact: {customer['contactName']}, Company: {customer['companyName']}, Phone: {customer['phone']}")

def main():
    customers = customersTable('northwindCustomers.txt')  # Load customers into a list
    options = {  # Dictionary of user choices to sorting/searching options
        '1': ('companyName', 1),  # Sort by companyName
        '2': ('contactName', 2),  # Sort by contactName
        '3': ('companyName', 1),  # Search by companyName
        '4': ('contactName', 2),  # Search by contactName
        '5': None  # Exit the program
    }

    while True:
        print("\nHello! Enter a number corresponding to what you want displayed (Enter '5' to exit).\n")
        print("1. Display customers sorted by company name")
        print("2. Display customers sorted by contact name")
        print("3. Search customers by company name")
        print("4. Search customers by contact name")
        print("5. Exit")
        
        userInput = input("\nChoice: ")
        
        if userInput in options:  # Check if the input is a valid option
            if userInput in ['1', '2']:  # If the user wants to display sorted customers
                sortedCustomers = sortCustomers(customers, options[userInput][0])  # Sort customers
                displayCustomers(sortedCustomers, options[userInput][1])  # Display sorted customers
            elif userInput in ['3', '4']:  # If the user wants to search for customers
                searchAttribute = options[userInput][0]  # Get the attribute to search by
                searchName = input(f"Enter the {'company' if userInput == '3' else 'contact'} name to search: ")  # Prompt for search term
                matchingCustomers = searchCustomers(searchName, customers, searchAttribute)  # Search for matching customers
                if matchingCustomers:  # If there are matching customers
                    print(f"\nHere are the customer records for '{searchName}':")  # Inform the user of the results
                    displayCustomers(matchingCustomers, options[userInput][1])  # Display matching customers
                else:  # If no customers are found
                    print(f"No customers found for {'company' if userInput == '3' else 'contact'} name '{searchName}'.")  # Inform the user
            elif userInput == '5':  # If the user chooses to exit
                print("Thank you for checking out the customers of Northwind!")
                break  # Exit the loop
        else:  # If the input is invalid
            print("Invalid choice. Please try again.")  # Prompt the user to try again

if __name__ == "__main__":
    main()
