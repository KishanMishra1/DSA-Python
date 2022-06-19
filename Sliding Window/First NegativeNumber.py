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


n=8
arr=[12,-1,-7,8,-15,30,16,28]
i=0
k=3
kis=k
s=[]
while(i<n-2):
    count=0
    res=arr[i:k]
    for m in range(len(res)):
        count+=1
        if res[m]<0:
            s.append(res[m])
            break
        if count==kis:
            s.append(0)
    i+=1
    k+=1
print(s)











