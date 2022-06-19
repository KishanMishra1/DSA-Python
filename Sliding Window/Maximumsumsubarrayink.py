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


mx=0

k=3
arr=[2,5,1,8,2,9,1]
i=0
while(i<len(arr)):
    res=arr[i:k]
    mx=max(mx,sum(res))
    i+=1
    k+=1
print(mx)













