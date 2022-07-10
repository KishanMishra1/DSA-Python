#Maximum element from all the subarrays of size k
arr=[1,3,-1,-3,5,3,6,7]
k=3
i,j=0,0
v=[]
res=[]
while(i<len(arr) and j<len(arr)):
    res.append(arr[j])
    if j-i+1==k:
        v.append(max(res))
        res.pop(0)
        i+=1
    j+=1
print(v)
