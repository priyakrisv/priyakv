def sumOfAP(a,d,n):
 sum=0
 i=0
 while i<n:
  sum=sum+a
  a=a+d
  i=i+1
  return sum
  n=int(input("Enter any value:"))
  a=int(input("Enter any value:"))
  d=int(input("Enter any value:"))
    print(sumOfAP(a,d,n))
