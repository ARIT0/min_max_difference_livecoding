def minMax(array):
    
    x = 0
    z = 1

    for x in range(len(array)-1):
        if array[x] > array[x+1]:
            maxValue = array[x]
            #if x == len(array)-1:
                #break
        #return maxValue
    
    for y in range(len(array)-1):
        if array[y] < array[z]:
            z = array[y]
            minValue = array[z]
            
        #return minValue
    
    diff = maxValue - minValue
    return(diff)
    

def main():
    array = [1,2,33,4,5,32]
    # (input("What is the array/list?")) #in order to do this you must loop through 
                                        # with the number of item that you want to 
                                        # enter in the list, then one by one add them.
    print(minMax(array))

if __name__ == "__main__":
    main()