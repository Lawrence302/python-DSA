# searching algorithms

# linear search

numbers = [1,2,3,4,5,6,7,8,9,10]

def linear_search(numbers,value):
    for i in  range(len(numbers)):
        if numbers[i] == value:
            print(f'number found at position : {i}')
            return

    print(" number not found ")

linear_search(numbers,12)