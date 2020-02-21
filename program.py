from models import Library


def solve(fileObj):
    # foreach library - sort the books
    libraries = fileObj.libraries

    for lib in libraries:
        lib.booksIds = sorted(lib.books, key=lambda b: -b.score)

    # sort the libraries
    libraries = sorted(libraries, key=libraryScore)

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


def libraryScore(lib):
    # return lib.signUpTime
    sum = 0
    numOfBooks = len(lib.books)
    for book in lib.books:
        sum += book.score
    return (sum / numOfBooks) / \
        (lib.signUpTime + numOfBooks / lib.bookOutput)
