# selection sort - loop in a loop. O(n^2) - array at every step

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # range: start at current + 1, stop at length of arr
        for j in range(cur_index + 1, len(arr)):
            # if smallest > loop cycle j position in array
            if arr[smallest_index] > arr[j]:
                # if true, set smallest to j
                smallest_index = j

        # TO-DO: swap
        # Your code here
        # unpacking and assigning to a tuple
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    made_a_swap = True

    # while there is a swap
    while made_a_swap:
        # set made_a_swap to false
        made_a_swap = False

        # start at 0 to element before end of length of array
        for i in range(0, len(arr) - 1):
            # counter
            j = i + 1

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                # swap was made. set to true
                made_a_swap = True

    return arr


"""
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def count_sort(arr, maximum=0):
    return arr
