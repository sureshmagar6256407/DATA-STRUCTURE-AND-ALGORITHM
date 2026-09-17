"""
Method 1: Quick Sort (Lomuto Partition Scheme)
Quick Sort is an efficient, divide-and-conquer algorithm. It works by selecting a pivot element from the array, partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot, and recursively sorting the sub-arrays.

Step-by-Step Code Execution
1- Select Pivot & Initialize Pointer (partition())
The last element (num[high]) is picked as the pivot (spelled povert in the code). Pointer i starts before low (low - 1) to mark the boundary of elements smaller than or equal to the pivot.

2-Rearrange Elements (for j in range(low, high))
Loop j scans from low to high - 1. Whenever num[j] <= pivot, i is incremented and num[i] is swapped with num[j], moving smaller elements to the left side.

3-Place Pivot in Correct Position (num[i + 1] <-> num[high])
After scanning, the pivot is swapped with num[i + 1]. The pivot is now at its final sorted position (pivot_index = i + 1).

4-Recursive Sorting (quick_sort())
The algorithm recursively calls quick_sort on the left sub-array (low to pivot_index - 1) and the right sub-array (pivot_index + 1 to high).

Execution Trace
Initial Array: [64, 34, 25, 5, 22, 11, 90, 12]

Step 1 -> Pivot: 12 | Partitioning [64, 34, 25, 5, 22, 11, 90, 12]
          Swapped elements <= 12 to left side, then placed pivot at index 2.
          Array state: [5, 11, 12, 64, 22, 34, 90, 25]

Step 2 -> Left Sub-array  : [5, 11] (Already partitioned)
Step 3 -> Right Sub-array : Pivot: 25 | Partitioning [64, 22, 34, 90, 25]
          Placed pivot at index 4.
          Array state: [5, 11, 12, 22, 25, 34, 90, 64]

Step 4 -> Sub-array : Pivot: 64 | Partitioning [34, 90, 64]
          Placed pivot at index 6.
          Array state: [5, 11, 12, 22, 25, 34, 64, 90]

Sorted Array : [5, 11, 12, 22, 25, 34, 64, 90]

Complexity Analysis
-Time Complexity:
Best Case:O(n log n)
(Occurs when the pivot consistently divides the array into two equal halves)
Average Case:O(n log n)
Worst Case: O (n^2)
(Occurs when the pivot is always the smallest or largest element, e.g., already sorted array)
Auxiliary Space Complexity:O (n log n)
(Due to the recursive function call stack)
"""
def partition(num,low,high) : 
    povert  = num[high]
    i   = low  - 1   

    for  j  in range (low,high) : 
        if num[j] <= povert : 
            i += 1   
            num[i] , num[j]  = num[j] , num[i]
    num[i +1] , num[high]  = num[high] ,num[i + 1]
    return i + 1

def quick_sort(num, low = 0 , high = None) : 
    if high is None : 
        high  = len(num)-1   

    if low < high : 
        povert_index  = partition(num,low,high)   
        quick_sort(num,low, povert_index -1)
        quick_sort(num,povert_index + 1, high)

num  =  [64, 34, 25, 5, 22, 11, 90, 12] 
quick_sort(num)
print(num)