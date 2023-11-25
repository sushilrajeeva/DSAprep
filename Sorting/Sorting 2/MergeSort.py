def mergeSort(data: list, start: int, end: int):
    
    # base condition 
    if(start >=  end):
        return 
    
    mid = (start + end) // 2
    # Sort Left
    mergeSort(data, start, mid)
    # Sort Right
    mergeSort(data, mid+1, end)
    # Merging arrays
    merge(data, start, mid, end)
        

def merge(data: list, start: int, mid: int, end: int):
    
    # building a temporary array to avoid modifiying original content
    temp = []
    
    left = start
    right = mid + 1
    
    # while both of sub-arrays have values, then try and merge them in sorted order
    while(left <= mid and right<= end):
        
        if(data[left] <= data[right]):
            temp.append(data[left])
            left+=1
            
        else:
            temp.append(data[right])
            right+=1
       
    # While there is data to triverse
    # Add the rest of values from the left sub-arrays into the result 
    while (left<= mid):
        temp.append(data[left])
        left+=1
    
    # Add the rest of values from the right sub-arrays into the result    
    while(right <= end):
        temp.append(data[right])
        right+=1
        
        
    # Replacing the Original with copy data
    for i in range(start, end+1):
        data[i] = temp[i-start]
        
        
        
input_data = [-5, 20, 10, 3, 2, 0]
print("Given array", input_data) 
mergeSort(input_data, 0, len(input_data) - 1)
print("After merge sort :", input_data)

    