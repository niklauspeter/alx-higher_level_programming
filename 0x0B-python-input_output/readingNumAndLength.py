import os

with open("mydata.txt", mode = "w", encoding = "utf-8") as myfile:

    myfile.write("some text\n some more text\n some textingness")

with open("mydata.txt", encoding = "utf-8") as  myfile:

    lineNum = 1
    totalWordLength = 0
    while True:

        line = myfile.readline()
        
        Linelength = 0
        for i in line:
            Linelength += 1
        
        if not line:
            print("\n")
            break

        print("line", lineNum, " : ", line, end="")
        print ("linelength :", Linelength, "\n", end="")
        lineNum += 1
        totalWordLength += Linelength
print("total length", totalWordLength)
        
