arr = [5,9,8,4,3,1,2,6]
print(arr)
def selection_sort(lis):
    for i in range(len(lis)):   # this loop defines our outer passes through the array, starting with "i=zero"
        index = i               # this is our "marker" index, a placeholder for the lowest value found
        for j in range(i+1, len(lis)):  # this loop defines our inner passes through the array, each time "forgetting" the prior digit (i+1)
            if lis[index] > lis[j]:     # if our marker value > the value j from the inner pass...
                index = j       # ...then shift the marker to the value j; this always puts the marker value on the lowest "j"
        lis[i], lis[index] = lis[index], lis[i]     # now that marker is on lowest "j" from inner loop, swap the marker with "i" from outer loop
    print(lis)
selection_sort(arr)
