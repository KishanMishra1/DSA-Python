arr=[22,44,55,11,33,5]
print("Original Array :{}".format(arr))
n=len(arr)
print("Bubble Sorting -->")
for i in range(n-1):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted Array :{}".format(arr))
