import os
from models.library import Library
from models.file import File

IN_FOLDER = './in/'

def fileToObject(filename):
    with open(filename, 'r') as fn:
        lines = fn.readlines()
        numOfBooks, numOfLibs, deadline = map(int, lines[0].split(' '))
        bookScores = list(map(int, lines[1].split(' ')))
        libs = []
        
        for i in range(2,len(lines),2):
            libBooks, signUp, booksOutput = map(int, lines[i].split(' '))
            books = list(map(int, lines[i+1].split(' '))) 
            libs.append(Library(libBooks, signUp, booksOutput, books))

        return File(numOfBooks, numOfLibs, deadline, bookScores, libs)

def testFiles():
    for name in os.listdir(IN_FOLDER):
        testFile(IN_FOLDER + name)

def testFile(filepath):
    obj = fileToObject(filepath)
    print(calculateFinalScore(obj))
    
if __name__ == "__main__":
    # testFile(IN_FOLDER + 'a_example.txt')
    print(fileToObject(IN_FOLDER + 'a_example.txt'))