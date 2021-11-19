import random

def Fibonacci(n): 
    if n<0: 
        raise ValueError
    elif n==0: #
        return 0
    elif n==1: #base occasion
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2)

n = int(input("Please enter the number to reach: "))
def main(n):
    lineCount = 1
    totalCount = 0
    while lineCount != n+1:
        for i in range(0, lineCount):
            print(lineCount, end="")
            totalCount+=lineCount
        lineCount+=1
        print("")
    print(f"total count of ints = {totalCount}")
    return

main(n)

y = int(input("# of num: "))
def Fibonacci(y):
    x = 2
    num1 = 0
    num2 = 1
    while x < y:
        z = num1 + num2
        print(z)
        num1 = num2
        num2 = z
        x += 1
    print(num2/num1)


 









        

