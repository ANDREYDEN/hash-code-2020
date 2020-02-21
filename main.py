import test
import program

if __name__ == "__main__":
    inputs = test.readFiles()
    libScore = program.libScoreBySignup
    solutions = [program.solve(inputObj, libScore) for inputObj in inputs]
    test.printScores(inputs, solutions)
    test.submitAll(solutions)
