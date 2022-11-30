def binsearch(lst, number):
    low = 0
    high = len(lst)-1
    for i in range(len(lst)):
        mid = (low + high)//2
        if low == high:
            return -1
        elif lst[mid] == number:
            return mid
        
        elif lst[mid] > number:
            high = mid
            
        else:
            low = mid + 1
            
lst = [0, 2, 5, 7, 10, 35]
print(binsearch(lst, 1))
