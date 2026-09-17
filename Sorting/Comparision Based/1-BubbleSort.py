#METHOD  -1    
# We have unsorted list   num  , it's have 6 item and and it's lenght is 6   we use for loop i  , its run 0 TO 4 and n-1  is not count now ,, then we declare swap variable  now we initialize false because its now sort . the inner loop run n -i-1  it's mean n=6 - i= it's iteration from 0 its value is  0 and -1  , = 6-0-1  = 5    . and we compare first num[0] value 7 to num[1] = 12 if num[0] > num[1] then excute  9 line code and swap gona be true     .. if now swap  then break mean its not print the same code 
def bubbleSort(num) :  
    n   = len(num)
    for i  in range (n-1) : 
        swap  = False  
        for j  in range (n - i - 1) : 
            if num[j] > num[j +1] : 
                num[j] , num[j +1]   = num[j +1] , num[j]
                swap  = True  
        if not swap : 
            break  

    print(num)
num  = [7, 12, 9,15, 11, 50]  
bubbleSort(num)


#METHOD - 2   
# its all processing but we simple use while loop 
def bubbleSort1(num1) : 
    n   = len(num1)
    i  = 0   
    while i < n - 1 : 
        for j  in range (n- i -1) : 

            if num1[j] > num1[j +1] : 
                num1[j] , num1[j +1]  = num1[j +1] , num1[j]  
        i += 1 
    print(num1)
num1 = [2,4,56,2,7,9,6,1] 
bubbleSort1(num1)