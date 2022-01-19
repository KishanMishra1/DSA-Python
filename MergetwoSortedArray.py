def merge(A, B):
    i,j = 0,0
    while i<len(A) and j<len(B):
    if A[i]>=B[j]:
        A.insert(i,B[j])
        i += 1
        j += 1
        elif A[i]<B[j]:
            i+=1
        if j<len(B) and i>=len(A):
            A.extend(B[j:])
    return A
