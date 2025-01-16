class Library:
    def __init__(self):
        #Initialize empty list of books
        self.books = []

    def add_book(self, title):
        '''Adding book by title'''
        try:
            if isinstance(title,str):
                if title == '': #Ensuring title is non-empty string
                    print('Please input valid book title')
                else:
                    self.books.append(title)
                    print(f'Your book is successfully added to the collection!\nBook Added:{title}\nHere are the list of your collection:{self.books}')
            else:
                print('Please input valid book title')
        except TypeError:
            print('Please input valid book title')
        except ValueError:
            print('Please input valid book title.')

    def remove_book(self,title):
        '''Remove book by title'''
        try:
            if isinstance(title,str):
                if title in self.books: #Checking if book is in the collection
                    self.books.remove(title)
                else:
                    print(f'Book is not in the collection. Current collection:{self.books}')
            else:
                print('Please input valid book title.')
        except TypeError:
            print('Please input valid book title.')
        except ValueError:
            print('Please input valid book title.')
    
    def display_books(self):

        print('Here are books in your collection:')
        for index, book in enumerate(self.books, start=1):
            print(f'{index}. {book}')

library1 = Library()
library1.add_book('1984')
library1.add_book('Milk and honey')
library1.remove_book('1984')
library1.add_book('To kill a mockingbird')
library1.display_books()
