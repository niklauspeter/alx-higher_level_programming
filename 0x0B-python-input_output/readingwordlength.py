import os

with open("mydata.txt", mode = "w", encoding = "utf-8") as myfile:

    myfile.write("some text\n some more text\n some textingness")

with open("mydata.txt", encoding = "utf-8") as  myfile:

    lineNum = 1

    while True:

        line = myfile.readline()
        
        if not line:
            print("\n")
            break
        
        #split() to create iterable list containing individual worlds

        wordlist = line.split()
        
        #use len() to find number of words in each line

        print("Number of words :", len(wordlist))

        #loop count characters in word list

        charCount = 0
        for word in wordlist:
            for char in word:
                charCount += 1
        #find average of characters in each word in a line
        
        avgnumchars = charCount/len(wordlist)
        print("avg word length : {: .2}".format(avgnumchars))

        lineNum += 1