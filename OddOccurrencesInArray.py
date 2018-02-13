def solution(A):
    A.sort()
    p = 1
    for i, item in enumerate(A):
        if i == len(A)-1:
            if p % 2:
                return A[i]
            #print p
            break
        else:
            if A[i] == A[i+1]:
                p += 1
            else:
                if p != 1:
                    if p % 2:
                        return A[i]
                    #print p
                else:
                    if p % 2:
                        return A[i]
                    #print p
                p = 1
