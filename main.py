import test
import program

if __name__ == "__main__":
    inputs = test.readFiles()
    solutions = [program.solve(inputObj) for inputObj in inputs]
    test.printScores(inputs, solutions)
    test.submitAll(solutions)
