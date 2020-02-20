def calculateFinalScore(solution, file):
    currentDay = 0
    score = 0
    booksScanned = []
    librariesSignedUp = []

    #for each libraby
    for x in range(0, solution.nbOfLibraries):
        #get library
        library = file.libraries[solution.library[x].libraryId]
        
        #skip if too long sign up
        if (currentDay + library.signUpTime) > file.nbOfDays
            continue
        
        #else add sign up time
        currentDay += library.signUpTime

        #for each day left, add books
        for y in range( currentDay, file.nbOfDays):
            