# Magic methods, also known as dunder methods, allow you to define how objects of a class behave with built-in Python operations.

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author} has {self.num_pages} pages." 
    

    def __eq__(self, other):
        return (self.title == other.title and 
                    self.author == other.author and 
                    self.num_pages == other.num_pages)
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 500)
book3 = Book("1984", "George Orwell", 328)

print(book1)  # Output: The Great Gatsby by F. Scott Fitzgerald has 180 pages.
print(book2 == book1)  # Output: False
print(book2 > book3)  # Output: False