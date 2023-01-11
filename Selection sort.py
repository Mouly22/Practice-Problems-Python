#Selection sort
def selection(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    print(lst)
    
lst = [2, 5, 1, 0, -9, 4, 10, 3, 2, 20]
selection(lst)