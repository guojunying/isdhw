def bsearch(data,target):
    begin = 0
    if data[0] == target:
        return none

    end = len(data)-1
    while(begin < end):
        mid = begin + (end - begin)//2
        if data[mid]>target:
            end = mid - 1
        elif data[mid] <target:
            begin = mid + 1
        else:
            return mid

    if(begin == end):
        if(target == data[begin]):
            return begin
        else:
            return -1
        
