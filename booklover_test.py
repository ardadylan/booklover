import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        bl = BookLover("Arda", "arda@gmail.com", "fiction")
        bl.add_book("Yes", 5)
        self.assertTrue("Yes" in bl.book_list['book_name'].values)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bl = BookLover("Arda", "arda@gmail.com", "fiction")
        bl.add_book('Flyguy', 5)
        bl.add_book('Flyguy', 4)
        self.assertEqual(len(bl.book_list[bl.book_list['book_name'] == 'Flyguy']), 1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        bl = BookLover("Arda", "arda@gmail.com", "fiction")
        bl.add_book("Dog and Guy", 4)
        self.assertTrue(bl.has_read("Dog and Guy"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bl = BookLover("Arda", "arda@gmail.com", "fiction")
        bl.add_book("Treebook", 2)
        self.assertFalse(bl.has_read("The Hobbit"))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        bl = BookLover("Arda", "arda@gmail.com", "fiction")
        bl.add_book("Wow", 4)
        bl.add_book("Wowow", 5)
        bl.add_book("Wowowow", 5)
        self.assertEqual(bl.num_books_read(), 3)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        bl = BookLover("Arda", "arda@gmail.com", "fiction")
        bl.add_book("five", 5)
        bl.add_book("four", 4)
        bl.add_book("three", 3)
        bl.add_book("two", 2)
        fav_books_df = bl.fav_books()
        self.assertTrue(all(fav_books_df['book_rating'] > 3))     
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)