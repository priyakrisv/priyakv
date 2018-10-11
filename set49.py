m=[]
p=int(input("Enter number of elements:"))
for i in range(1,p+1):
    l=int(input("Enter element:"))
    m.append(l)
m.sort()
print("Largest element is:",m[p-1])
