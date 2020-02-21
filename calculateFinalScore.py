def calculateFinalScore(inputObj, libs):
    currentDay = 0
    score = 0
    scanned = [False] * inputObj.nbOfBooks

    for lib in libs:

        # skip if the sign up will take too long
        if currentDay + lib.signUpTime > inputObj.nbOfDays:
            break

        # else add sign up time
        currentDay += lib.signUpTime

        # for each day left, for each book today, add books
        bookPos = 0
        virtualFuture = currentDay
        while bookPos < len(lib.scannedBooks) and virtualFuture < inputObj.nbOfDays:
            bookId = lib.scannedBooks[bookPos].id
            bookScore = lib.scannedBooks[bookPos].score
            if not scanned[bookId]:
                scanned[bookId] = True
                score += bookScore
            bookPos += 1

            # increase the day count if the we went through all the books for this day
            if bookPos % lib.bookOutput == 0:
                virtualFuture += 1

    return score
