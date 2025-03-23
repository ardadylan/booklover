import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        """
        Initialize object.
        """
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    
    def add_book(self, book_name, rating):
        """ 
        Add a book to the book_list

        Parameters:
        book_name (str)
        rating (int)

        Returns:
        None
        """
        # Check if book is already in the list
        if not self.book_list.empty and book_name in self.book_list['book_name'].values:
            print(f"{book_name} is already in the list.")
            return
        
        # Add the book to the list
        new_book = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [rating]
        })

        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1

    def has_read(self, book_name):
        """
        Check if book is already in the list
        
        Parameters:
        book_name (str)
        
        Returns:
        bool
        """
        return book_name in self.book_list['book_name'].values
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        """
        filter data frame for favorite books
        """
        return self.book_list[self.book_list['book_rating']>3]
    
    
if __name__ == '__main__':
    test_object = BookLover("Laura", "lauralikestoread@hotmail.com", "Horror")
    test_object.add_book("Vampire Hunter", 5)
    test_object.add_book("Gumpy", 2)
    print(test_object.has_read('Gumpy'))
    print(test_object.has_read('arda'))
    print(test_object.num_books_read())
    print(test_object.fav_books())
    
    