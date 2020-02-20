class Library:
    def __init__(self,libraryId ,nbOfBooks, signUpTime, bookOutput,books):
        self.libraryId = libraryId
        self.nbOfBooks = nbOfBooks
        self.signUpTime = signUpTime
        self.bookOutput = bookOutput
        self.books = books

    def __str__(self):
        res = f'{self.nbOfBooks} {self.signUpTime} {self.bookOutput} : '
        return res + str(self.books)


