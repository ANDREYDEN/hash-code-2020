def calculateFinalScore(solution, file):
    currentDay = 0
    score = 0
    booksScanned = []
    librariesSignedUp = []

    #for each libraby
    for x in range(solution.nbOfLibraries):
        #get library
        library = solution.libraries[x]
        libraryId = library.libraryId
        
        #skip scanned libraries
        if libraryId in librariesSignedUp:
            continue

        #skip if too long sign up
        if (currentDay + library.signUpTime) > file.nbOfDays:
            continue
        
        #else add libraryId and sign up time
        librariesSignedUp.append(libraryId)
        currentDay += library.signUpTime

        #for each day left, for each book today, add books
        for day in range( currentDay, file.nbOfDays):
            for bookId in range(0, library.bookOutput):
                #Skipped scanned books
                if bookId in booksScanned:
                    continue 
                #else add score
                booksScanned.append(bookId)
                score += file.bookScores[bookId]
    
    return score