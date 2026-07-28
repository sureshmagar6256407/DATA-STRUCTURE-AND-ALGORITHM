#METHOD 1  
'''
Insertion Sort builds the final sorted array one item at a time. It works similarly to the way you sort playing cards in your hands—taking one card from the unsorted side and shifting larger cards right until it finds the correct spot to insert it.

Step-by-Step Code Execution
1-Pick the Key Element (key = num[i])
Starting at index 1, the outer loop iterates through the unsorted section. It picks the current element as the key to be inserted into the sorted sublist on its left.

2-Compare and Shift (while j >= 0 and num[j] > key)
The inner while loop checks the sorted sublist from right to left (j = i - 1). As long as an element num[j] is greater than key, it shifts that element one position to the right (num[j + 1] = num[j]).

3-Insert Key (num[j + 1] = key)
Once a smaller or equal element is reached (or j hits -1), the key is inserted into the opened slot at j + 1.

4-Print State (print(num))
Outputs the state of the array after each pass to show how the sorted boundary grows from left to right.

Execution Trace
Plaintext

Initial Array: [64, 34, 25, 5, 22, 11, 90, 12]

Step 1 -> Key: 34 | Shifted 64             | Array: [34, 64, 25, 5, 22, 11, 90, 12]
Step 2 -> Key: 25 | Shifted 64, 34         | Array: [25, 34, 64, 5, 22, 11, 90, 12]
Step 3 -> Key: 5  | Shifted 64, 34, 25     | Array: [5, 25, 34, 64, 22, 11, 90, 12]
Step 4 -> Key: 22 | Shifted 64, 34, 25     | Array: [5, 22, 25, 34, 64, 11, 90, 12]
Step 5 -> Key: 11 | Shifted 64, 34, 25, 22 | Array: [5, 11, 22, 25, 34, 64, 90, 12]
Step 6 -> Key: 90 | Shifted none (90 > 64) | Array: [5, 11, 22, 25, 34, 64, 90, 12]
Step 7 -> Key: 12 | Shifted 90, 64, 34, 25, 22 | Array: [5, 11, 12, 22, 25, 34, 64, 90]

Sorted Array : [5, 11, 12, 22, 25, 34, 64, 90]
Complexity Analysis
Time Complexity:
-> Best Case:  O(n)
(Occurs when the array is already sorted; inner loop condition fails immediately)
-> Average Case : O(n^2)
-> Worst Case: O(n^2)
(Occurs when the array is sorted in reverse order; requires shifting all elements)

Auxiliary Space Complexity: O(1)
(In-place sorting algorithm with zero extra memory allocation)
'''


def insertionSort(num) : 
    n   = len(num)

    for i  in range (1,n) : 
        key  = num[i]   
        j  = i -1     

        while j >= 0 and num[j] > key : 
            num[j +1] = num[j]
            j -= 1 
        num[j +1]  = key   
        print(num)

num  =  [64, 34, 25, 5, 22, 11, 90, 12] 
insertionSort(num)