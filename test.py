import os


def readFiles():
    IN_FOLDER = './in'
    for name in os.listdir(IN_FOLDER):
        obj = readFile(IN_FOLDER + '/' + name)
        print(obj)


def readFile(name):
    with open(name, 'r') as fin:
        return fin.readlines()


if __name__ == "__main__":
    readFiles()
