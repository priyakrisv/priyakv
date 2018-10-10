name=input("enter name:")
k=0
with open (name,'r') as f:
for line in f:
words=line.split()
for i in words:
for letters in i:
if(letter.isspace):
k=k+1
print("occurances of blank spaces:")
print(k)
