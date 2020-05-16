def insertionSort(A):  
    count=0 
    for i in range(len(A)): 
        
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
                count=count+1
                
        # Swap the found minimum element with  
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i]
        
    return count

lst=[1, 2, 2, 4, 5]
print(insertionSort(lst))