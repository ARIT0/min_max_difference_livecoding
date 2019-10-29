def minMax(array):
    array = input("What is the array?")
    
    array = [1,2,3,4,5]
    x = 0
    for x in range(len(array)):
        if array[x] > array[x+1]:
            maxValue = array[x]
        return maxValue
    for y in range(len(array)):
        if array[y] < array[y+1]:
            minValue = array[y]
        return minValue

    diff = maxValue - minValue
    print(diff)

