import os
from models.library import Library
from models.file import File
from models.book import Book
from calculateFinalScore import calculateFinalScore
from program import solve

IN_FOLDER = './in/'
OUT_FOLDER = './out/'


def fileToObject(filename):
    with open(filename, 'r') as fn:
        lines = fn.read().splitlines()
        numOfBooks, numOfLibs, deadline = map(int, lines[0].split(' '))
        bookScores = list(map(int, lines[1].split(' ')))
        libs = []

        for i in range(2, len(lines), 2):
            if (lines[i] == ''):
                continue
            _, signUp, booksOutput = map(int, lines[i].split(' '))
            books = []
            for score, i in enumerate(lines[i+1].split(' ')):
                books.append(Book(int(i), int(score)))
            libs.append(Library(len(libs),
                                signUp,
                                booksOutput,
                                books,
                                []))

        return File(numOfBooks, numOfLibs, deadline, bookScores, libs)


def testFiles():
    for name in os.listdir(IN_FOLDER):
        testFile(IN_FOLDER + name)


def testFile(filepath):
    obj = fileToObject(filepath)
    solution = solve(obj)
    print(calculateFinalScore(solution, obj))


def solutionToFile(libs, filepath):
    with open(filepath, 'w') as fout:
        fout.write(str(len(libs)) + '\n')
        for lib in libs:
            fout.write(str(lib.id) + ' ' + str(len(lib.scannedBooks)) + '\n')
            fout.write(
                ' '.join(list(map(lambda book: str(book.id), lib.scannedBooks))) + '\n')


if __name__ == "__main__":
    # testFile(IN_FOLDER + 'a_example.txt')
    # print(fileToObject(IN_FOLDER + 'a_example.txt'))

    files = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt',
             'd_tough_choices.txt', 'e_so_many_books.txt', 'f_libraries_of_the_world.txt']
    for file in files:
        solution = solve(fileToObject(IN_FOLDER + file))
        solutionToFile(solution, OUT_FOLDER + file)
