def mergesort(arr):
    if len(arr)<=1:
        return
    mid=(len(arr))//2
    left=arr[:mid]
    right=arr[mid:]
    mergesort(left)
    mergesort(right)
    merge(left,right,arr)
    return arr

def merge(a,b,arr):
    len_a=len(a)
    len_b=len(b)
    i,j,k=0,0,0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while(i<len_a):
        arr[k]=a[i]
        i+=1
        k+=1
    while j< len_b:
        arr[k] =b[j]
        j+=1
        k+=1

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = mergesort(num_list)
print("After sorting:",sorted_list)
