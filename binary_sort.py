#Binary sort
def binary_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j]< lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    print(lst)

    
lst = [2, 4, 10, 100, 56, 21, 7, 7]
binary_sort(lst)
