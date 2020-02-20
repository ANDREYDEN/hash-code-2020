import os

IN_FOLDER = './in'
OUT_FOLDER = './out'


def readFiles():

    for name in os.listdir(IN_FOLDER):
        obj = readFile(IN_FOLDER + '/' + name)
        print(obj)


def readFile(name):
    with open(name, 'r') as fin:
        return fin.readlines()


def writeFile


if __name__ == "__main__":
    readFiles()
