
print("Enter 'x' for exit.");
str1 = input("Enter first string to concatenate: ");
if str1 == 'x':
   exit();
else:
    str2 = input("Enter second string to concatenate: ");
    str3 = str1 + str2;
    print("\nString after concatenation =",str3);
    print("Str 1 =",str1);
    print("Str 2 =",str2);
    print("Str 3 =",str3);
