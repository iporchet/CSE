num = int(input("Enter a whole number: "))

count = 0
while num != 0:
    count = count + 1
    # change 10 to two since it is base 2 
    num = num // 2
  
print("Number of digits in input is: ", count)