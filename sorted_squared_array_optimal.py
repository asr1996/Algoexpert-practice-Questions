def sortedSquaredArray(array):
    array2 = [0 for i in range(len(array))]
    i=0
    j=len(array)-1
    k=j
    while i<=j:
        if abs(array[i]) <= abs(array[j]):
            array2[k] = array[j] * array[j]
            j-=1
        else:
            array2[k] = array[i] * array[i]
            i+=1
        k-=1
    return array2
