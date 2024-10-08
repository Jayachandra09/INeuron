def Partition(arr, p, q):
    pivot = arr[p]
    i = p
    for j in range(i+1, q+1):
        if arr[j]<pivot:
            i+=1
            #Swap between the values of arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
        #Final swap between arr[i] and arr[p]
    arr[i], arr[p] = arr[p], arr[i]
    return i

def QuickSort(arr, p, q):
    if p<q:
        # Divide and Conquer Approach
        #1. Divide
        #Function calling for the partition part 
        mid = Partition(arr, p, q)
        #Recursive function call for the left sub tree
        QuickSort(arr, p, mid-1)
        #Recursive function call for the right sub tree
        QuickSort(arr, mid+1, q)
    return arr

#Driver Code
arr = [50, 70, 29, 67, 12, 15, 46, 100, 26, 29]
p = 0
q = len(arr)-1
result = QuickSort(arr, p, q)
print(result)
