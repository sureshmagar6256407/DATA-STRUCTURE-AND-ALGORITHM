#METHOD 1 : First of all we need two variable prev1 and prev2 where they store 0 and 1  ,  Using the loop  we iteration 1 TO 10 ,, and then we sum the  prev1 and prev2 store them current variable and print  first iteration value , then we again we pass the prev2 value in prev1 and current value on prev2   ,, its continue until the loop not end 
def fabbonaci (prev1, prev2) :    
    for i in range (10) : 
        current  = prev1  + prev2   
        print(current)
        prev1  = prev2  
        prev2   = current  
    
prev1   = 0  
prev2 = 1   
fabbonaci (prev1  , prev2)



print()
#METHOD - 2 :Using Recursion  
#It is same method of previous code but in this main part is recursion the function call itself when the condtion isnot satisfied
num1   = 0    
num2   = 1   
count  = 2
def fabbonacci1(num1,num2) : 
    global count  
    if count <= 10 : 
        newfibo  = num1  + num2  
        print(newfibo)
        num1  = num2  
        num2   = newfibo  
        count += 1 
        fabbonacci1(num1,num2)
    else : 
        return
fabbonacci1(num1,num2)


print()
#METHOD - 3 : Just implementation Formula 
#Here this code works with simple math formula  we pass F(n) parameter on loop  the it's run 0 TO 9 and   the conditon check if n value 1 or less than 1 or 0 its return simple n value  otherwise else condtion will be execute     
def F(n) :   
    if n <=1 : 
        return n 
    else : 
        return F(n-1)  + F(n-2)
for i  in range (10) : 
    print(F(i))