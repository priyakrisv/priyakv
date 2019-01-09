def checkDigits(n):  
 while (n>0):  
  if ((n % 10) % 2):  
    return False; 
   n =int(n/10);
return True;  
def largestNumber(n):  
 for i in range(n,-1,-1): 
 if (checkDigits(i)): 
            return i;
p =int(input("enter the number:"));  
print(largestNumber(p)); 
  
