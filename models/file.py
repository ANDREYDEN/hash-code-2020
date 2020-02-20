class File:
    def __init__(self, nbOfBooks, nbOfLibraries, nbOfDays, bookScores, libraries):
        self.nbOfBooks = nbOfBooks
        self.nbOfLibraries = nbOfLibraries
        self.nbOfDays = nbOfDays
        self.bookScores = bookScores
        self.libraries = libraries

    def __str__(self):
        res = f'{self.nbOfBooks}, {self.nbOfLibraries}, {self.nbOfDays}\n'
        res += str(self.bookScores)
        return res + str(list(map(str, self.libraries)))