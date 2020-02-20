class Library:
    def __init__(self, libraryId, nbOfBooks, signUpTime, bookOutput, booksIds, nbOfBooksScanned):
        self.libraryId = libraryId
        self.nbOfBooks = nbOfBooks
        self.signUpTime = signUpTime
        self.bookOutput = bookOutput
        self.booksIds = booksIds
        self.nbOfBooksScanned = nbOfBooksScanned

    def __str__(self):
        res = f'{self.nbOfBooks} {self.signUpTime} {self.bookOutput} : '
        return res + str(self.booksIds)

