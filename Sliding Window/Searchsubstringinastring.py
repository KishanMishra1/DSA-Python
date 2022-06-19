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


s="smanainterviewsmartbnb"
sr="sma"
km=""
for i in range(len(s)):
    for j in range(i+1,len(s)):
        k=s[i:j]
        #print(k)
        if k==sr:
            print("Substring Found !")
            print(f"Starting point {i} Ending Point {j}")












