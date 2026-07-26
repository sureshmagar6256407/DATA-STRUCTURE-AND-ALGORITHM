#Method -1   

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