import xml.sax

class BooksHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.books = []
        self.current = ""
        self.title = ""
        self.author = ""
        self.year = ""
        self.available = ""

    def startElement(self, name, attrs):
        self.current = name

    def characters(self, content):
        if self.current == "title":
            self.title += content.strip()
        elif self.current == "author":
            self.author += content.strip()
        elif self.current == "year":
            self.year += content.strip()
        elif self.current == "available":
            self.available += content.strip()

    def endElement(self, name):
        if name == "book":
            self.books.append({
                "title": self.title,
                "author": self.author,
                "year": self.year,
                "available": self.available
            })
            self.title = ""
            self.author = ""
            self.year = ""
            self.available = ""
        self.current = ""

    
handler = BooksHandler()
xml.sax.parse("books.xml", handler)

# Displays all the books from the xml file
print("\nAll the books we offer:\n")
for book in handler.books:
    print(f"{book['title']} by {book['author']} ({book['year']})\n")

# While loop for the user to repeatedly search by book title until they 'quit'
while True:
    # Get user input and remove extra spaces
    search = input("\nEnter a book title (enter 'quit' to end program): ").strip()
    if search.lower() == 'quit':
        break

    found = False
    for book in handler.books:
        title = book['title']
        # This following if statement allows the user to just enter parts of the title
        # if they do not want to enter the full title
        if search.lower() in title.lower():  
            author = book['author']
            year = book['year']
            avaText = book['available']
            availability = "Available" if avaText.lower() == 'true' else "Not Available"
            print(f"\nTitle: {title}")
            print(f"Author: {author}")
            print(f"Year: {year}")
            print(f"{availability}")
            found = True
            break

    if not found:
        print(f"\n'{search}' not found")
