def MergeProcedure(arr, i, mid, j):
    # Calculating the no. of elements in subarrays
    m = mid-i+1
    n = j-(mid+1)+1

    # Initialising the extra space
    left_subarray = [0]*m
    right_subarray = [0]*n

    # Copying elements to the Sub Arrays
    for indx in range(m):
        left_subarray[indx] = arr[i+indx]
    for indx in range(n):
        right_subarray[indx] = arr[(mid+1)+indx]

    p = 0
    q = 0
    k = i 
    while p<len(left_subarray) and q<len(right_subarray):
        if left_subarray[p]<right_subarray[q]:
            arr[k] = left_subarray[p]
            p+=1
            
        else:
            arr[k] = right_subarray[q]
            q+=1
        k+=1
    
    while p<len(left_subarray):
        arr[k] = left_subarray[p]
        p+=1
        k+=1
    while q<len(right_subarray):
        arr[k] = right_subarray[q]
        q+=1
        k+=1

def MergeSort(arr, i, j):
    if i<j:
        mid = i+(j-i)//2
        MergeSort(arr, i, mid)
        MergeSort(arr, mid+1, j)

        MergeProcedure(arr, i, mid, j)
    return arr

arr = [50, 70, 65, 13, 80, 62, 98, 27]
i = 0 
j = len(arr)-1
result = MergeSort(arr, i, j)
print(result)
