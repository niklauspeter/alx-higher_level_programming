import os

with open("mydata.txt", mode = "w", encoding = "utf-8") as myfile:

    myfile.write("some text\n some text\n some text")

with open("mydata.txt", encoding = "utf-8") as  myfile:

    lineNum = 1

    while True:

        line = myfile.readline()
        
        if not line:
            print("\n")
            break

        print("line", lineNum, " : ", line, end="")
        lineNum += 1
        
