n1=input("enter any number")
n2=input("enter any number")
n3=input("enter any number")
if((n1>=n2) and (n1>=n3)):
    largest=n1
elif((n2>=n1) and (n2>=n3)):
    largest=n2 
else:
    largest=n3
    print("the largest number between",n1,",",n2,",","and",n3,"is",largest)    
