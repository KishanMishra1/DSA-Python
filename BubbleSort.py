arr=[22,44,55,11,33,5]
print("Original Array :{}".format(arr))
n=len(arr)
print("Bubble Sorting -->")
for i in range(len(arr)-1):
    swapped=False
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if not swapped : #if the array is already sorted , break out the loop
        break
print("Sorted Array :{}".format(arr))
