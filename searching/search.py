# searching algorithms

# linear search

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
steps = 0

def linear_search(numbers,value):
    for i in  range(len(numbers)):
        if numbers[i] == value:
            print(f'number found at position : {i}')
            return

    print(" number not found ")

linear_search(numbers,12)

# binary search 0(logn)

def binary_search(numbers, value):
    start = 0
    end = len(numbers)-1
    middle = end//2
    
# the loop should run so long as the start index is less than the middle index
    while start <= middle:
        global steps
        steps = steps + 1
        print(f"start: {start}, middle: {middle}, end: {end}")
        print(f"step: {steps}")
       
        #check for the value
        if numbers[middle] == value:
            print(f"number found at index {middle}")
            return
        elif numbers[middle] < value:
            start = middle + 1
            middle = (end + start)//2
        else:
            end = middle -1
            middle = (end + start)//2

    print("the number you are looking for was not found ")


binary_search(numbers,5)