lower=int(input("enter any number:"))
upper=int(input("enter any number:"))
for num in range(lower,upper+1)
order=len(str(num))
 sum=0
 temp=num
  while(temp!=0):
   digit=temp%10
   sum+=digit**order
   temp=temp//10
   if sum==num:
    print("armstrong number")
     else:
      print("not armstrong number)
