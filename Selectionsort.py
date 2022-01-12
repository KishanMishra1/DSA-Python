arr=[22,44,55,11,33,5]
print("Original Array :{}".format(arr))
n=len(arr)
print("Selection Sorting -->")
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if arr[min]>arr[j]:
            min=j
    arr[min],arr[i]=arr[i],arr[min]
print("Sorted Array :{}".format(arr))
