import json

with open('books.json') as f:
    data = json.load(f)

# Displays all the books from the json file
print("\nAll the books we offer:\n")
for book in data['books']:
    print(f"{book['title']} by {book['author']} ({book['year']})\n")

# While loop for the user to repeatedly search by book title until they 'quit'
while True:
    # Get user input and remove extra spaces
    search = input("\nEnter a book title (enter 'quit' to end program): ").strip() 
    if search.lower() == 'quit':
        break

    found = False
    for book in data['books']:
        # This following if statement allows the user to just enter parts of the title
        # if they do not want to enter the full title
        if search.lower() in book['title'].lower():
            availability = "Available" if book['available'] else "Not Available"
            print(f"\nTitle: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"{availability}")
            found = True
            break

    if not found:
        print(f"\n'{search}' not found")
