#Insertion sort:
def insertion(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j-1]> lst[j]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
    print(lst)
    
lst = [2, 5, -4, 1, 0, -9, 4, 10, 3, 2, 20,5]
insertion(lst)