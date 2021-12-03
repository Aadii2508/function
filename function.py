def countWordsFromFile():
    fileName= input("enter the file name: ")

    numberOfWords= 0

    file= open(fileName, 'r')
    for lines in file:
        words= lines.split()
        numberOfWords= numberOfWords + len(words)
    print("Number of Words: ", numberOfWords)
  
countWordsFromFile()

