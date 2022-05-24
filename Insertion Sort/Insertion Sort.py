arr = [1,6,3,4,2,5,7,9]; #ARRAY

def insert_sort(arr):
    for i in range(1, len(arr)):
        while arr[i-1]> arr[i] and i > 0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i-=1

#SORT ARRAY
insert_sort(arr)
#PRINT ARRAY
print(arr)
