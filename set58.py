p = int(input('How many numbers: '))
total_sum = 0
for n in range(p):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/p
print('Average of ', p, ' numbers is :', avg)
