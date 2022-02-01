def equation_solver(num1, num2, num3, num4, num5, num6):
  answ1 = 0
  answ2 = 0

  for x in range(-10, 10):
    for y in range(-10, 10):
      target1 = (num1*x) + (num2*y)
      target2 = (num4*x) + (num5*y)

      if (target1 == num3) and (num6 == target2):
        is_answer = True
        answ1 = x
        answ2 = y
        break

      else:
        is_answer = False 

    if (is_answer == True):
      break

  if (is_answer == True):
    print("x = ",x,"y = ", y)

  if (is_answer == False):
    print("No solution")
  
        


''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
equation_solver(a, b, c, d, e, f)

