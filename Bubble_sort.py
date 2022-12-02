#Bubble sort:
def bubble(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)
    
    
    
lst = [2, 5, 1, 0, -9, 4, 10, 3, 2, 20]
bubble(lst)