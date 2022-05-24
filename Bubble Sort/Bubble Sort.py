arr = [1,4,2,7,5,8,6,3,9] #ARRAY

def bubble(arr):

    indexing_length = len(arr) - 1 #INTEGER
    sorted = False #BOOLEAN

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

#PRINT UNSORTED
print(arr)     
#PRINT SORTED      
print(bubble(arr))

