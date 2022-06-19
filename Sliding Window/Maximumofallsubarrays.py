import sys
from math import *
input = sys.stdin.readline
#Template Kishan Mishra
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def instr():
    s = input()
    return(list(s[:len(s) - 1]))
def inn():
    return(map(int,input().split()))


arr=[1,3,-1,-3,5,3,6,7]
k=3
i=0
ms=[]
while(i<len(arr)-2):
    res=arr[i:k]
    ms.append(max(res))
    i+=1
    k+=1
print(ms)













