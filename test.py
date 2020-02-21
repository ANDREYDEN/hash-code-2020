import os
from models import Library, Input, Book
from calculateFinalScore import calculateFinalScore
from program import solve

IN_FOLDER = './in/'
OUT_FOLDER = './out/'
FILE_NAMES = 'abcdef'


def fileToObject(filename):
    with open(filename, 'r') as fin:
        lines = fin.read().splitlines()
        numOfBooks, numOfLibs, deadline = map(int, lines[0].split(' '))
        bookScores = list(map(int, lines[1].split(' ')))
        libs = []

        for i in range(2, len(lines), 2):
            if (lines[i] == ''):
                continue
            _, signUp, booksOutput = map(int, lines[i].split(' '))
            books = []
            for idx in map(int, lines[i+1].split(' ')):
                books.append(Book(idx, bookScores[idx]))

            libs.append(Library(len(libs), signUp, booksOutput, books, []))

        return Input(numOfBooks, deadline, libs)


def readFiles():
    return [fileToObject(IN_FOLDER + filename) for filename in os.listdir(IN_FOLDER)]


def printScore(filename, score):
    print(f'{filename.ljust(10, " ")}: {score}')


def readAndTestOne(filename):
    inputObj = fileToObject(filename)
    solution = solve(inputObj)
    printScore(calculateFinalScore(inputObj, solution), filename)


def printScores(inputs, solutions):
    for inputObj, solution, filename in zip(inputs, solutions, FILE_NAMES):
        printScore(filename, calculateFinalScore(inputObj, solution))


def submitToFile(libs, filepath):
    with open(filepath, 'w') as fout:
        fout.write(str(len(libs)) + '\n')
        for lib in libs:
            fout.write(str(lib.id) + ' ' + str(len(lib.scannedBooks)) + '\n')
            fout.write(
                ' '.join(list(map(lambda book: str(book.id), lib.scannedBooks))) + '\n')


def submitAll(answers):
    for libs, fileName in zip(answers, FILE_NAMES):
        submitToFile(libs, OUT_FOLDER + fileName + '.txt')
