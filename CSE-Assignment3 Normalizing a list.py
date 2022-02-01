def normalize_list(list):
    largest_number = list[0]

    for x in range(0, len(list)):
        if (list[x] > largest_number):
            largest_number = list[x]

    for x in range(0, len(list)):
        list[x] = list[x]/largest_number

    return list


list = []

num_of_floats = int(input())

for x in range(0, num_of_floats):
    
    usr_input = float(input())
    list.append(usr_input)

final_list = normalize_list(list)

for x in range(0, len(list)):
    print(f'{list[x]:.2f}')
