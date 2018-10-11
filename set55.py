m = int(input("Please Enter any Number: "))
Count = 0
while(m > 0):
    m = m // 10
    Count = Count + 1

print("\n Number of Digits in a Given Number = %d" %Count)
