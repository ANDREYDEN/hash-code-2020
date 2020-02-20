class Library:
    def __init__(self, id, signUpTime, bookOutput, books, scannedBooks):
        self.id = id
        self.signUpTime = signUpTime
        self.bookOutput = bookOutput
        self.books = books
        self.scannedBooks = scannedBooks

    def __str__(self):
        res = f'{self.nbOfBooks} {self.signUpTime} {self.bookOutput} : '
        return res + str(self.booksIds)
