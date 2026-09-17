
'''
Method 1: Dutch National Flag Algorithm (3-Way Partitioning)
The Dutch National Flag (DNF) algorithm sorts an array containing three distinct values (commonly 0s, 1s, and 2s) in a single pass. It uses three pointers (low, medium, and high) to partition the array into three sections: zeros on the left, ones in the middle, and twos on the right.

Step-by-Step Code Execution
1-Initialize Three Pointers (low, medium, high)
low and medium start at 0, while high starts at len(num) - 1. The area before low stores 0s, between low and high stores 1s, and after high stores 2s.

2- Process 0s (num[medium] == 0)
Swaps num[medium] with num[low], then increments both low and medium to expand the zeros boundary on the left.

3-Process 1s (num[medium] == 1)
Leaves the element in place and increments medium to expand the ones boundary.

4-Process 2s (num[medium] == 2)
Swaps num[medium] with num[high], then decrements high to expand the twos boundary on the right. (Note: medium is not incremented here because the newly swapped element at medium needs to be evaluated next).


*Initial Array: [1, 2, 1, 0, 2, 1, 0]
Step 1 -> Val: 1 | medium=0, high=6 | No swap            | Array: [1, 2, 1, 0, 2, 1, 0]
Step 2 -> Val: 2 | medium=1, high=6 | Swapped (2 <-> 0)  | Array: [1, 0, 1, 0, 2, 1, 2]
Step 3 -> Val: 0 | medium=1, high=5 | Swapped (0 <-> 1)  | Array: [0, 1, 1, 0, 2, 1, 2]
Step 4 -> Val: 1 | medium=2, high=5 | No swap            | Array: [0, 1, 1, 0, 2, 1, 2]
Step 5 -> Val: 0 | medium=3, high=5 | Swapped (0 <-> 1)  | Array: [0, 0, 1, 1, 2, 1, 2]
Step 6 -> Val: 1 | medium=4, high=5 | No swap            | Array: [0, 0, 1, 1, 2, 1, 2]
Step 7 -> Val: 2 | medium=4, high=5 | Swapped (2 <-> 1)  | Array: [0, 0, 1, 1, 1, 2, 2]

=> Sorted Array : [0, 0, 1, 1, 1, 2, 2]

Time Complexity you can just search on internet .
'''
def NDF (num) :   
    low =  0  
    medium  = 0  
    high  = len(num) -1    

    while medium <= high :  
        if num[medium] ==  0 : 
            num[low],num[medium] = num[medium] , num[low] 
            low += 1  
            medium += 1   
        elif num[medium] == 1 : 
            medium += 1   
        else :  
            num[medium] , num[high] = num[high]  , num[medium]
            high -= 1  
    print(num)




num  = [1,2,1,0,2,1,0]
NDF(num)