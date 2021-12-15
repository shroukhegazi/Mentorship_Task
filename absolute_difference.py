import sys

x = int(input())
array = list(map(int, input().split()))
array.sort()
sum=array[1]-array[0]
for i in range(0,x-1):
    if (array[i+1]-array[i]<sum):
        sum= array[i+1]-array[i]

print(sum)
