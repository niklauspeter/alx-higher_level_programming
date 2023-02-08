import os

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
         ans = fib(num - 1) + fib(num -2 )
         return ans

#ask how many bumbers they want
numFibValues = int(input("How many fib fibonacci values should be found: "))

#loop whie calling for each new number
i = 1

while i < numFibValues:
    fibValue = fib(i)
    print(fibValue)

    i += 1
print("All done")

#print result and increment