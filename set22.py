M=input("Enter any number:")
try:
if(M==str(M)[::-1]):
  print("The given number is palindrome")
 else:
  print("The given number is not a palindrme")
 except valueError:
  print("That's not avalid number, try again!")
