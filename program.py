from models import Library
import statistics


def solve(fileObj, libComparator):
    # foreach library - sort the books
    libraries = fileObj.libraries

    for lib in libraries:
        lib.booksIds = sorted(lib.books, key=lambda b: -b.score)

    # sort the libraries
    libraries = sorted(libraries, key=libComparator)

    # keep track of processed books
    finished = [False] * fileObj.nbOfBooks

    # create the solution object
    for lib in libraries:
        for book in lib.books:
            if not finished[book.id]:
                finished[book.id] = True
                lib.scannedBooks.append(book)

    libraries = list(filter(lambda lib: len(lib.scannedBooks) > 0, libraries))

    return libraries


def libScoreBySignup(lib):
    return lib.signUpTime


def libScoreByMean(lib):
    mean = statistics.mean([book.score for book in lib.books])
    return mean / (lib.signUpTime + len(lib.books) / lib.bookOutput)
