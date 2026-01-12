from book import Book

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
         self.books.append(book)

    def show_books(self):
        if not self.books:
            print("Няма книги в библиотеката.")
        else:
            print("\n--- Всички книги ---")
            for i, book in self.books:
                print(f"{i}. {book}")

    
    
        