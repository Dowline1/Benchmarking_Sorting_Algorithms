# Packages required for generating random arrays
#  and timing sorting algorithm 
import random
import time

# Sizes of random arrays to be generated
array_size_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]

# Variables to store avg times for each array 
# size by algorithm
bubble_sort_times = []
heap_sort_times = []
bucket_sort_times = []
shell_sort_times = []
gnome_sort_times = []

# Function to generate random integer list adapted 
# from project specification
def random_array(n):
    array = []
    for i in range(0, n):
        array.append(random.randint(0, 100))
   
    return array

# ---------- Bubble Sort Algorithm Start ----------#
# Bubble Sort Algorithm adapted from Optimized: 
# https://www.geeksforgeeks.org/bubble-sort/

def bubbleSort(arr): 
    n = len(arr) 
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break
# ---------- Bubble Sort Algorithm End ----------#


# ---------- Heap Sort Algorithm Start ----------#
# Heap Sort Algorithm adapted from:
# https://www.geeksforgeeks.org/heap-sort/
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest)


def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 
# ----------Heap Sort Algorithm End ----------#


# ----------Bucket Sort Algorithm Start ----------#
# Bucket Sort Algorithm adapted from:
# https://www.sanfoundry.com/python-program-implement-bucket-sort/
def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
# ----------Bucket Sort Algorithm End ----------#

# ----------Shell Sort Algorithm Start ----------#
# Shell Sort Algorithm adapted from:
# https://www.geeksforgeeks.org/shellsort/
def shellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap //= 2
# ----------Shell Sort Algorithm End ----------#

# ----------Gnome Sort Algorithm Start ----------#
# Gnome Sort Algorithm adapted from:
# https://www.geeksforgeeks.org/gnome-sort-a-stupid-one/
def gnomeSort( arr, n): 
    index = 0
    while index < n: 
        if index == 0: 
            index = index + 1
        if arr[index] >= arr[index - 1]: 
            index = index + 1
        else: 
            arr[index], arr[index-1] = arr[index-1], arr[index] 
            index = index - 1
  
    return arr
# ----------Gnome Sort Algorithm End ----------#



# Main Program used to call sorting algorithms 
# and store the execution times of each including the average of 10 runs
def main():

    # Global Variables as detailed above 
    global array_size_list
    global bubble_sort_times
    global heap_sort_times
    global bucket_sort_times
    global shell_sort_times
    global gnome_sort_times

    while True:

            # Used as method to start benchmarking
            choice = input("Type 'run' and Enter to Benchmark Sorting Algorithms, type 'quit' to exit: ")

            if choice == "run":

                # Runs each array size one by one
                for i in array_size_list:
                    
                    # Counters to ensure algorithm runs 10 times
                    # resets after each array size has run 10 times
                    # run_times stores run times for each of 10 runs
                    bubble_counter = 0
                    heap_counter = 0
                    bucket_counter = 0
                    shell_counter = 0
                    gnome_counter = 0


                    # Start times of algorithm
                    start_time = time.time()

                    # While loop runs algorithm 10 times Bubble Sort
                    while bubble_counter < 10:
                        
                        # Generates the array for each run/array size
                        test_array = random_array(i)

                        # Executes Bubble Sort Algorithm
                        bubbleSort(test_array)

                        # Increase counter by 1
                        bubble_counter = bubble_counter + 1
                        
                    # End times of algorithm
                    end_time = time.time()
                    
                    # Time elapsed to complete sort algorithm
                    time_elapsed = end_time - start_time

                    # Appends average time of the 10 runs for the algorithm
                    # including for each array size    
                    bubble_sort_times.append(time_elapsed/10)
                    

                    # Start times of algorithm
                    start_time = time.time()

                    # While loop runs algorithm 10 times Heap Sort
                    while heap_counter < 10:
                        
                        # Generates the array for each run/array size
                        test_array = random_array(i)

                        # Executes Heap Sort Algorithm
                        heapSort(test_array)

                        # Increase counter by 1
                        heap_counter = heap_counter + 1

                    # End times of algorithm
                    end_time = time.time()
                    
                    # Time elapsed to complete sort algorithm
                    time_elapsed = end_time - start_time

                    # Appends average time of the 10 runs for the algorithm
                    # including for each array size    
                    heap_sort_times.append(time_elapsed/10)


                    # Start times of algorithm
                    start_time = time.time()

                    # While loop runs algorithm 10 times Bucket Sort
                    while bucket_counter < 10:
                        
                        # Generates the array for each run/array size
                        test_array = random_array(i)

                        # Executes Bucket Sort Algorithm
                        bucketSort(test_array)

                        # Increase counter by 1
                        bucket_counter = bucket_counter + 1

                    # End times of algorithm
                    end_time = time.time()
                    
                    # Time elapsed to complete sort algorithm
                    time_elapsed = end_time - start_time

                    # Appends average time of the 10 runs for the algorithm
                    # including for each array size    
                    bucket_sort_times.append(time_elapsed/10)


                    # Start times of algorithm
                    start_time = time.time()

                    # While loop runs algorithm 10 times Shell Sort
                    while shell_counter < 10:
                        
                        # Generates the array for each run/array size
                        test_array = random_array(i)

                        # Executes Shell Sort Algorithm
                        shellSort(test_array)

                        # Increase counter by 1
                        shell_counter = shell_counter + 1

                    # End times of algorithm
                    end_time = time.time()
                    
                    # Time elapsed to complete sort algorithm
                    time_elapsed = end_time - start_time

                    # Appends average time of the 10 runs for the algorithm
                    # including for each array size    
                    shell_sort_times.append(time_elapsed/10)


                    # Start times of algorithm
                    start_time = time.time()

                    # While loop runs algorithm 10 times Gnome Sort
                    while gnome_counter < 10:
                        
                        # Generates the array for each run/array size
                        test_array = random_array(i)

                        # Executes Gnome Sort Algorithm
                        gnomeSort(test_array, len(test_array))

                        # Increase counter by 1
                        gnome_counter = gnome_counter + 1

                    # End times of algorithm
                    end_time = time.time()
                    
                    # Time elapsed to complete sort algorithm
                    time_elapsed = end_time - start_time

                    # Appends average time of the 10 runs for the algorithm
                    # including for each array size    
                    gnome_sort_times.append(time_elapsed/10)

                for i in bubble_sort_times:
                    print("Bubble", i)

                for i in heap_sort_times:
                    print("Heap", i)

                for i in bucket_sort_times:
                    print("Bucket", i)

                for i in shell_sort_times:
                    print("Shell", i)

                for i in gnome_sort_times:
                    print("Gnome", i)

            
            if choice == "quit":
                break






# Runs main Program Tree Function
if __name__ == "__main__":
    main()