import unittest
'''Meng-import module unittest untuk menjalankan function Unit Testing'''

from h8dsft_oop import Book, LibraryCatalogSystem
'''Meng-import Function Book dan LibraryCatalogSystem yang diperoleh dari
file script python lain dalam satu folder yang sama dengan nama 'h8dsft_oop'. '''

class TestLibraryCatalogSystem(unittest.TestCase):
    ''' Membuat class Test Case Parent untuk unittest.TestCase'''

    def setUp(self):
        '''Function ini berguna untuk membuat instance self.library dari
        LibraryCatalogSystem() yang dapat diakses secara global'''

        self.library = LibraryCatalogSystem()

    def test_addBook(self):
        '''Function ini berguna untuk melakukan pengetesan terhadap function
        untuk penambahan buku kedalam list storage (penampungan data)'''

        self.library.addBook("Dilan: Dia Adalah Dilanku Tahun 1990", "Pidi Baiq", 1)
        self.library.addBook("Crazy Rich Asian", "Kevin Kwan", 2)
        self.assertEqual(len(self.library.catalog), 2)

    def test_removeBook(self):
        '''Function ini berguna untuk melakukan pengetesan terhadap function
        removeBook untuk menghapus buku.'''
        self.library.addBook("Dilan: Dia Adalah Dilanku Tahun 1990", "Pidi Baiq", 1)
        self.library.addBook("Crazy Rich Asian", "Kevin Kwan", 2)
        self.library.removeBook(2)
        self.assertEqual(len(self.library.catalog), 1)

if __name__=='__main__':
    unittest.main()