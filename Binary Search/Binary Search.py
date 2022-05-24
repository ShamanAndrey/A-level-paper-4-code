arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] #ARRAY

searchVal = 5 #INTEGER

def binary_search(Sequence : list, item : int):

    begin_index = 0 #INTEGER
    end_index = len(Sequence) #INTEGER

    while begin_index <= end_index:
        midpoint = begin_index + (begin_index + end_index)//2
        midpoint_value = Sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif midpoint_value < item:
            begin_index = midpoint - 1
        else:
            end_index = midpoint + 1

print(binary_search(arr,searchVal))
