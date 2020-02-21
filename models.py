class Input:
    def __init__(self, nbOfBooks, nbOfDays, libraries):
        self.nbOfBooks = nbOfBooks
        self.nbOfDays = nbOfDays
        self.libraries = libraries

    def __str__(self):
        res = f'{self.nbOfBooks}, {self.nbOfLibraries}, {self.nbOfDays}\n'
        res += str(self.bookScores)
        return res + str(list(map(str, self.libraries)))


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


class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
