'''
TIME COMPLEXITY  : O(d.(n + b))



'''



import pickletools


num = [170, 45, 75, 90, 802, 24, 2, 66]


def counting_sort(num ,exp) : 
    n  = len(num)

    output  = [0] * n  

    count   = [0] * 10  

    #Counting frequency  

    for i in range  (0, n) : 
        index = num[i] // exp  
        count[index % 10] += 1    

    #counting the frequency  

    for j  in range (1,10) : 
        count[j]  += count[j - 1]

    #finding the position  

    l  =  n - 1 
    while l >= 0 : 
        index  = num[l] // exp  
        output[count[index % 10] -1] = num[l]
        count[index % 10] -= 1 
        l -= 1 

    #exchange the position  
    for m  in range (0 , len(num)) : 
        num[m] = output[m]





def radix_sort (num) : 
    max_val  = max(num)

    exp  = 1  

    while max_val / exp  >= 1 :   
        counting_sort(num , exp)
        exp *= 10

radix_sort (num)
print(num)