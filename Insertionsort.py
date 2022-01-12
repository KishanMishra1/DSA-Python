arr=[22,44,55,11,33,5]
print("Original Array :{}".format(arr))
n=len(arr)
print("Insertion Sorting -->")
for i in range(1,n):
    key=arr[i]
    j=i-1
    while arr[j]>key and j >=0:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print("Sorted Array :{}".format(arr))
