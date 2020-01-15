class Library:
    def __init__(self, name):
        self.name = name
        self.books = list()

    def set_address(self, address):
        self.address = address
        
    def list_books(self):
        for book in self.books:
            print(book.title)
    
    def add_book(self, new_book):
        self.books.append(new_book)

if __name__ == '__main__':
    print("This is the file with the Library class")
