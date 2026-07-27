#Method -1    
'''
This variation of Selection Sort sorts the array in ascending order by building the sorted portion from right to left. In each pass, it finds the maximum element in the unsorted left portion and swaps it into its correct position at the end.

--> Step-by-Step Code Execution
1.Set Boundary from Right to Left (for i in range(n - 1, 0, -1))
The outer loop moves backward from the last index down to index 1. Index i marks the target position where the largest unsorted element should end up.
2.Find the Maximum Element (max_index = 0 & Inner Loop)
Assumes the element at index 0 is the largest, then uses the inner loop (j) to scan up to index i to find the actual maximum value's index (max_index).
3-Swap into End Position (if max_index != i)
If the maximum element is not already at target index i, it swaps the element at max_index with the element at i.
4-Print State (print(num))
Outputs the array state after each valid swap to visually track the sorting progress from right to left.

Execution Trace
Plaintext
Initial Array: [64, 34, 25, 5, 22, 11, 90, 12]

Step 1 -> Max found: 90  | Swapped (12 <-> 90) | Array: [64, 34, 25, 5, 22, 11, 12, 90]
Step 2 -> Max found: 64  | Swapped (12 <-> 64) | Array: [12, 34, 25, 5, 22, 11, 64, 90]
Step 3 -> Max found: 34  | Swapped (11 <-> 34) | Array: [12, 11, 25, 5, 22, 34, 64, 90]
Step 4 -> Max found: 25  | Swapped (22 <-> 25) | Array: [12, 11, 22, 5, 25, 34, 64, 90]
Step 5 -> Max found: 22  | Swapped (5 <-> 22)  | Array: [12, 11, 5, 22, 25, 34, 64, 90]
Step 6 -> Max found: 12  | Swapped (5 <-> 12)  | Array: [5, 11, 12, 22, 25, 34, 64, 90]

Sorted Array : [5, 11, 12, 22, 25, 34, 64, 90]

Complexity Analysis
Time Complexity:
Best Case: O(n^2)
Average Case :O(n^2) 
Worst Case :O(n^2)
(Scanning for the maximum in diminishing sublists still requires nested loops)

Auxiliary Space Complexity: O(1)
(In-place sorting algorithm with zero extra space memory usage)
'''


def selection_reverse(num) : 
    n  = len(num)

    for  i in range (n-1 , 0 , -1) : 
        max_index  = 0  
        for j in range (1, i+1) : 
            if num[j] > num[max_index] : 
                max_index  = j   

        if max_index != i : 
            num[max_index] , num[i]  = num[i] , num[max_index]
            print(num)
num  =  [64, 34, 25, 5, 22, 11, 90, 12]   
selection_reverse(num)