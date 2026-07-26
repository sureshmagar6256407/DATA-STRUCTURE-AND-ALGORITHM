#Method -1   
'''
Selection Sort is an in-place, comparison-based sorting algorithm. It divides the array into a sorted sublist (built left-to-right) and an unsorted sublist, repeatedly picking the smallest element from the unsorted section and moving it to the end of the sorted section.Step-by-Step Code ExecutionSet Search Boundary (for i in range(n - 1))The outer loop tracks the current position i being sorted, separating the sorted elements on the left from the unsorted elements on the right.Find the Minimum Element (min_index = i & Inner Loop)Assumes num[i] is the minimum, then uses the inner loop (j) to scan the rest of the array to locate the actual smallest value's index (min_index).Swap into Position (if min_index != i)If a smaller value was found, it swaps the element at i with the minimum element at min_index.Print State (print(num))Outputs the array after every valid swap to track sorting progress.

Execution TracePlaintextInitial Array: [64, 34, 25, 5, 22, 11, 90, 12]
Step 1 -> Min found: 5   | Swapped (64 <-> 5)  | Array: [5, 34, 25, 64, 22, 11, 90, 12]
Step 2 -> Min found: 11  | Swapped (34 <-> 11) | Array: [5, 11, 25, 64, 22, 34, 90, 12]
Step 3 -> Min found: 12  | Swapped (25 <-> 12) | Array: [5, 11, 12, 64, 22, 34, 90, 25]
Step 4 -> Min found: 22  | Swapped (64 <-> 22) | Array: [5, 11, 12, 22, 64, 34, 90, 25]
Step 5 -> Min found: 25  | Swapped (64 <-> 25) | Array: [5, 11, 12, 22, 25, 34, 90, 64]
Step 6 -> Min found: 64  | Swapped (90 <-> 64) | Array: [5, 11, 12, 22, 25, 34, 64, 90]

Sorted Array : [5, 11, 12, 22, 25, 34, 64, 90]

Complexity Analysis
Time Complexity:
- Best Case: O(n^2)
-Average Case : O(n^2)
- Worst Case : O(n^2)
(Requires nested loops regardless of initial order to find the minimum)
-Auxiliary Space Complexity: O(1)
(In-place sorting algorithm requiring no extra memory allocation)
'''
def selectionSort1(num) :  
    n  = len(num)

    for i  in range (n - 1) : 
        min_index  = i  
        for j  in range (i+1,n) : 
            if num[j] < num[min_index] : 
                min_index  = j  

        if min_index != i : 
            num[i] , num[min_index]  = num[min_index] , num[i]
            print(num)


num  =  [64, 34, 25, 5, 22, 11, 90, 12] 
selectionSort1(num)