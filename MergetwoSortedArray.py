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

def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    a, b, write_index = m-1, n-1, m + n - 1

    while b >= 0:
        if a >= 0 and A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1

        write_index -= 1
