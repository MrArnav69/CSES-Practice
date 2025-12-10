n = int(input())

numS = input()

numList = list(map(int, numS.strip().split()))
totalSum = n*(n+1)//2
currentSum = sum(numList)

missingNum = totalSum-currentSum
print(missingNum)
