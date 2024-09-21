for i in range(1,10):
    for j in range(10-i):
        print(i, end=" ")
    print()

def printpyramid(n):
        for i in range(1,n+1):
            for j in range(n-i):
                print(j, end=" ")
            print()

printpyramid(5)
