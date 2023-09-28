# TASK ANSWER

class Book:
    '''Class ini berguna untuk mendefinisikan object berupa buku-buku yang diinput oleh user.'''

    def __init__(self, title, author, uniqueID):
        '''Function ini berguna untuk meng-initialize atribute berupa title, author, dan unique identifier (uniqueID).'''

        self.title = title
        self.author = author
        self.uniqueID = uniqueID

    def __str__(self):
        '''function ini berguna untuk membentuk tampilan string yang dapat dibaca secara jelas saat mencetak objek Book'''

        return f"{self.title} by {self.author} (ID: {self.uniqueID})"

class LibraryCatalogSystem:
    '''Class ini memiliki isi berupa function mengenai catalog dari Library meliputi menambahkan, mencari, mengapus dan menampilkan buku'''

    def __init__(self):
        '''fucntion ini berguna untuk menginialisasikan list yang bernama 'catalog'.
        List ini berisikan title, author, dan ID buku.'''

        self.catalog = []

    def addBook(self, title, author, uniqueID):
        '''Fucntion ini sebagai fitur untuk menambahkan buku ke dalam storage list
        yang dimana di dalam prosesnya ada pengecekan '''

        try:
            # Mengecek apakah terjadi redudansi/ uniqueID yang diiput sudah terdaftar.

            if any(book.uniqueID == uniqueID for book in self.catalog):
                raise ValueError("Unique ID already in use.")
            newAddedBook = Book(title, author, uniqueID)
            self.catalog.append(newAddedBook)
            print(f"Book added: {newAddedBook}")
        except ValueError as e:
            print(f"Error: {e}")

    def searchByTitle(self, title):
        '''Function ini berfungsi sebagai fitur untuk melakukan pencarian buku didalam katalog
        berdasarkan judul buku'''

        foundBooks = [book for book in self.catalog if title.lower() in book.title.lower()]
        #statement untuk mencari berdasarkan judul

        if foundBooks:
            print("Books found by title:")
            for book in foundBooks:
                print(book)
        else:
            print("No books found by title.")

    def searchByAuthor(self, author):
        '''Function ini berfungsi sebagai fitur untuk melakukan pencarian buku didalam katalog
        berdasarkan penulis/ author buku'''

        foundBooks = [book for book in self.catalog if author.lower() in book.author.lower()]
        #statement untuk mencari berdasarkan author

        if foundBooks:
            print("Books found by author:")
            for book in foundBooks:
                print(book)
        else:
            print("No books found by author.")

    def removeBook(self, uniqueID):
        '''Function ini berfungsi sebagai fitur untuk mengahpus buku dari catalog menggunakan
        method .remove() dan program memilih berdasarkan uniqeID bukunya'''

        try:
            for book in self.catalog:
                if book.uniqueID == uniqueID:
                    self.catalog.remove(book)
                    print(f"Book removed: {book}")
                    return
            raise ValueError("Book not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def displayCatalog(self):
        '''Funciton ini berfungsi untuk menampilkan daftar buku/ catalog buku'''
        
        if self.catalog:
            print("Library Catalog:")
            for book in self.catalog:
                print(book)
        else:
            print("The catalog is empty.")

# Test Input Output

'''Membuat objek library untuk dapat menggunakan metode-metode 
yang didefinisikan dalam kelas LibraryCatalogSystem, 
seperti addBook, searchByTitle, searchByAuthor, removeBook, dan displayCatalog'''
library = LibraryCatalogSystem()

library.addBook("Dilan: Dia Adalah Dilanku Tahun 1990", "Pidi Baiq", 1)
library.addBook("Harry Potter and The Philosopher's Stone", "J.K Rowling", 2)
library.addBook("Crazy Rich Asian", "Kevin Kwan", 3)

library.displayCatalog()

library.searchByTitle("Dilan")
library.searchByTitle("harry potter")
library.searchByAuthor("Kevin Kwan")

library.removeBook(2)
library.removeBook(4)  # Mencoba menghapus yang tidak ada dalam list storage

library.displayCatalog()