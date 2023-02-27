def bubbleSort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                flag = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag == False:
            break
    return arr

inp_b = open('input3.txt', 'r')
out_b = open('output3.txt', 'w')
l1 = inp_b.readlines()
valus = l1[1].split()
arr = []
for elm in valus:
    arr.append(elm)


target = bubbleSort(arr)
for ex in target:
    out_b.write(ex+' ')

#I have used here a flag to indetify whether any swap happens or not. If there is no swapping, the 'break' statement stops the loop and this is how we can achieve big-O(n) for the best case.