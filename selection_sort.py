arr = [5,9,8,4,3,1,2,6]
print(arr)
def selection_sort(lis):
    for i in range(len(lis)):   # pass through the full array
        index = i
        for j in range(i+1, len(lis)):  # pass through the array above the current i-value comparing each of the numbers(j) to the current i-value
            if lis[index] > lis[j]:
                index = j       # here we find the index of the new minimum value 
        # swap the found element (j) with the first element
        lis[i], lis[index] = lis[index], lis[i]
    print(lis)
selection_sort(arr)
