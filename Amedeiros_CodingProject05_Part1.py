### CSC6013 - Coding Project 05 - Part 1
### Copyright Alexander Medeiros 11/27/2023

"""
This program is designed to sort an array of numbers into ascending order, by sorting the largest numbers. 

An argument is provided to the program 'selectionSort(A)' in the form of an array 'A'

The array length is stored in a variable 'n' for use in the program. 

An outer for loop is established, and loops for each k in range n-1, 0, -1

Variables called 'comparisons' and 'swaps' are initialized at zero to store a count while the program compares and swaps during sorting. 

A variable called 'maxIndex' is initialized as the kth index

Another inner for loop is established, for each j in range 'k'

A comparison count is incremented for each iteration of the inner loop when a comparison is performed for items in the array

inside the inner loop, an if condition compares the jth index of the array to the maxIndex value in the array, (A[j] > A[maxIndex])

When this condition is met, the variable is updated maxIndex = j

A swap is then performed on the items in the array, so sort the largest item in teh correct ascending order, and a swap count is incremented

The partial sorted array is printed, along with the comparison and swap counter. 

After the loops complete the comparisons through each item in the array, the final sorted array is printed. 

Usage example:
    selectionSort(A)

Assignment instructions:

    # 1) a) Write Python code for the selection sort algorithm to sort an array into ascending order, but
    # modify the code in the class notes to do three things:

    # i) After k iterations through the outer loop, the k LARGEST elements should be sorted
    # rather than the k SMALLEST elements.

    # ii) On each iteration through the outer loop, count the number of times two array
    # elements are compared and the number of times two array elements are swapped.
    # Reinitialize these counters to zero at the beginning of each iteration.

    # iii) After each iteration through the outer loop, print three things: the partially sorted
    # array, the number of comparisons on this iteration, and the number of swaps on this
    # iteration. After the kth iteration, you should see that the k largest elements have been
    # placed into the last k slots of the array.

    # b) Check your algorithm on the problem instances:

    # A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
    # A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
    # A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]`

"""


# Method to sort an array in ascending order using the largest values
def selectionSort(A):

    n = len(A) # measure length of array 'A' and store in variable 'n'

    for k in range(n-1,0,-1): # for loop, for each k in range

        comparisons = 0 # initialize comparison counter
        swaps = 0   # initialize swap counter
        maxIndex = k # initialize variable maxIndex as k

        for j in range (k): # for loop, for each j in range k

            comparisons+=1 # increment comparison for each loop where a comparison is made

            if (A[j] > A[maxIndex]): # if condition, compare Jth value in array with maxIndex value
                maxIndex = j # if condition is met, set maxIndex value to jth item in array for proper sorting ascension

        A[k], A[maxIndex] = A[maxIndex], A[k] # perform swap
        swaps+=1 # increment swap counter

        print(f'A =', A, 'Comparisons:', comparisons, 'Swaps:', swaps) # print the partial swapped array, comparison is swap counter

    print(f'\nFinal sorted array:', A,'\n') # print the final sorted array

A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39] # test case 1
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44] # test case 2
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6] # test case 3

selectionSort(A1) # run sorting algorithm on test case 1
selectionSort(A2) # run sorting algorithm on test case 2
selectionSort(A3) # run sorting algorithm on test case 3
