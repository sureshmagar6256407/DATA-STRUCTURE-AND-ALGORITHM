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