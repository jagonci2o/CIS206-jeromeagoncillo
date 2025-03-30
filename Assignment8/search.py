import csv

def customersTable(file_path):
    customersInfo = []  # Initializes an empty list to store the customer data as tuples.

    with open(file_path, 'r') as file:
        customerInfoReader = csv.reader(file, delimiter=',')
        # Creates a CSV reader object that will iterate over lines in the given CSV file.
        # The delimiter parameter shows that commas are used to separate values in the file.

        next(customerInfoReader)  # Skips the header

        for row in customerInfoReader:
            # Repeats over each following row in the CSV file except the header
            customersInfo.append(tuple(row))  # Store each row as a tuple
            # Converts the current row (list) into a tuple so the data of
            # customers can not be modified but we can use the tuple to
            # sort and search customers

    return customersInfo
    # Returns the 'customers' list, which now contains tuples of customer data from the CSV file.

def sortCustomers(customersInfo, index):
    if index == 1:
        # Sort by company name
        sortedCustomers = sorted(customersInfo, key=lambda customer: customer[1])
    elif index == 2:
        # Sort by contact name
        sortedCustomers = sorted(customersInfo, key=lambda customer: customer[2])
    else:
        raise ValueError("Invalid index for sorting. Use 1 for company name or 2 for contact name.")
    
    return sortedCustomers

def searchCustomers(name, customersInfo, index):
    # Searches for customers by company or contact name
    matching_customers = [customer for customer in customersInfo if name.lower() in customer[index].lower()]
    return matching_customers

def displayCustomers(customers, order):
    for customer in customers:
        if order == 1:
            # Display in this order, if by company name: company name, contact name, and phone number
            print(f"Company: {customer[1]}, Contact: {customer[2]}, Phone: {customer[9]}")
        elif order == 2:
            # Display in this order, if by contact name: contact name, company name, and phone number
            print(f"Contact: {customer[2]}, Company: {customer[1]}, Phone: {customer[9]}")

def main():
    customers = customersTable('northwind.txt')
    userInput = ''
    # I have it so the user will enter numbers 1-5 for what they what to do
    while userInput != '5':
        print("\nHello! Enter a number corresponding to what you want displayed (Enter '5' to exit).\n")
        print("1. Display customers sorted by company name")
        print("2. Display customers sorted by contact name")
        print("3. Search customers by company name")
        print("4. Search customers by contact name")
        print("5. Exit")
        userInput = input("\nChoice: ")

        if userInput == '1':
            print("\nHere are the customers sorted by company name.")
            sorted_customers = sortCustomers(customers, 1)
            displayCustomers(sorted_customers, 1)
        elif userInput == '2':
            print("\nHere are the customers sorted by contact name.")
            sorted_customers = sortCustomers(customers, 2)
            displayCustomers(sorted_customers, 2)
        elif userInput == '3':
            company_name = input("Enter the company name to search: ")
            matching_customers = searchCustomers(company_name, customers, 1)
            if matching_customers:
                print(f"\nHere are the customer records from company, '{company_name}':")
                displayCustomers(matching_customers, 1)
            else:
                print(f"No customers found for company name '{company_name}'.")
        elif userInput == '4':
            contact_name = input("Enter the contact name to search: ")
            matching_customers = searchCustomers(contact_name, customers, 2)
            if matching_customers:
                print(f"\nHere are the customer records from contact, '{contact_name}':")
                displayCustomers(matching_customers, 2)
            else:
                print(f"No customers found for contact name '{contact_name}'.")
        elif userInput == '5':
            print("Thank you for checking out the customers of Northwind!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
