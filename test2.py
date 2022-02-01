user_input= '1 2 3,2 4 6,3 6 9'
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

for x in mult_table:
    for y in range(0,len(x)):
        if y == len(x) - 1:    
            print(x[y])

        else:
            print(x[y], " | ", end='')

    print("\n")

   