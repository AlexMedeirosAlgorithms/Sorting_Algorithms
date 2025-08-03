### CSC6013 - Coding Project 05 - Part 2
### Copyright Alexander Medeiros 11/27/2023

"""
This program is designed to sort an array into ascending order, modified to exit early when the sorting is completed to minimize unessecary sorting iterations. 

The method 'bubbleSort(A)' is defined to accept an argument in the form of an array called 'A'

The length of the array 'A' is stored in a variable 'n' for use in the algorithm

Variables 'total_comparisons' and 'total_swaps' are initialized for counting the total iterations and operations performed on the array while sorting. 

An outer for loop is run, for each k in range n-1, the length of the array minus one to provide an absolute index value for each item in the array

Variables 'comparisons' and 'swaps' are initialized for counting operations within the relative inner loops.

An inner for loop is run, for each j in range of n-k-1

A comparison value is incremented, and an if condition compares the jth value in the array to determine if its value is greater than the neighbor j+1, (A[j]> A[j+1])
 
If the condition is met, a swap is performed and the swap value is incremented

The partial sorted array is printed along with the 'comparison' and 'swap' counter

The 'total_comparisons' and 'total_swaps' are also updated with the 'comparison' and 'swap' counts to track a total count of each 

if the 'swaps' value is ever equal to 0, the loop is broken and the algorithm is exited

The total counts are then printed for the user

Usage example:
    bubbleSort(A)

Assignment instructions:

    # 2) a) Write Python code for the bubble sort algorithm to sort an array into ascending order, but
    # with the possibility of an early exit if there are no swaps on some iteration through the outer
    # loop. Modify the code in the class notes to do four things:

    # i) On each iteration through the outer loop, count the number of times two array elements
    # are compared and the number of times two array elements are swapped. Reinitialize these
    # counters to zero at the beginning of each iteration.

    # ii) After each iteration through the outer loop, print three things: the partially sorted array,
    # the number of comparisons on this iteration, and the number of swaps on this iteration.
    # After the kth iteration, you should see that at least the k largest elements have “bubbled
    # up” into the last k slots of the array.

    # iii) If there are no swaps on some iteration through the outer loop, the array is now sorted,
    # so terminate the algorithm.

    # iv) When the algorithm concludes (after n-1 iterations or after an early exit), display the
    # total number of comparisons of array elements and the total number of swaps required to
    # sort the array.

    # b) Check your algorithm on the problem instances:

    # A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
    # A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
    # A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
"""

# method to sort an array into ascending order using a bubble-sort approach
def bubbleSort(A):
    n = len(A) # store the length of the array in a variable 'n'
    total_comparisons = 0 # initialize a total comparison counter
    total_swaps = 0 # initialize a total swap counter

    for k in range(n-1): # loop for each k in range, which are the indexes of the array 
        
        comparisons = 0 # initialize a comparison counter
        swaps = 0 # initialize a swap counter

        for j in range (n-k-1): # loop for each j in range n-k-1

            comparisons+=1 # increment the comparison count
            
            if (A[j]> A[j+1]): # if condition, if jth element of array is greater than its neighbor j+1

                A[j], A[j+1] = A[j+1], A[j] # perform swap
                swaps+=1 # increment swap counter

        print(f'A =', A, 'Comparisons:', comparisons, 'Swaps:', swaps) # print the partial sorted array, comparison and swap counts

        total_comparisons += comparisons # update the total counts
        total_swaps += swaps # update the total counts

        if swaps == 0: # check to see if a swap is 0, and break the loop if condition is met

            print(f'\nArray is now sorted. Exiting the algorithm.')
            break

    # Display the total number of comparisons and swaps
    print(f'Total Comparisons: {total_comparisons}')
    print(f'Total Swaps: {total_swaps}')
    print("")


A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52] # test case 4
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63] # test case 5
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99] # test case 6

bubbleSort(A4) # run sorting algorithm on test case 4
bubbleSort(A5) # run sorting algorithm on test case 5
bubbleSort(A6) # run sorting algorithm on test case 6