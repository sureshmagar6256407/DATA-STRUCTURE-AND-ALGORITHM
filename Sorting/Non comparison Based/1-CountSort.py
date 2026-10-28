#method  1 
'''
this is a non comparison sort . it works basically finding the biggest value than we create empty list where  its index 0 to max value index the we count frequency of number . then next we found the prefix sum recent value - previous value its gives us to position of the number than last loop do the place the number their exactly position 


so you can search about countsort and read document online
'''


def countSort (num) : 
    n  = len (num)

    maxval = max(num)

    count  = [0] * (maxval + 1)

    for i in  num : 
        count [i] += 1  

    for j in range (1 , maxval + 1) : 
        count[j] +=count[j - 1]

    ans  = [0] * n 

    for k in range (n - 1 , -1 , -1) : 
        val  = num[k]
        ans[count[val] - 1] = val  
        count[val] -= 1 

    print(ans)
num  =  [64, 34, 25, 5, 22, 11, 90, 12] 

countSort(num)