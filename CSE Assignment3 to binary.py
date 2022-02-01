def int_to_reverse_binary(integer_value):
    output = ""
    
    while (integer_value > 0):
        output += str(integer_value % 2)
        integer_value = integer_value // 2

    return output

def string_reverse(input_string):
    new_string = ""

    for x in range(len(input_string)-1, -1, -1):
        new_string += input_string[x]

    return new_string

if __name__ == '__main__':
    usr_input = int(input())

    print(string_reverse(int_to_reverse_binary(usr_input)))