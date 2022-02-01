# Define your functions here
def is_list_mult10(my_list):
    for x in my_list:
        if (x % 10) >= 1:
            is_mult = False
            break
        else:
            is_mult = True

    return is_mult

def is_list_no_mult10(my_list):
    for x in my_list:
        if x % 10 == 0:
            is_not_mult = False
            break

        else:
            is_not_mult = True

    return is_not_mult

if __name__ == '__main__':
    # Type your code here.
    len_of_list = int(input())
    mltples = []

    for x in range(0, len_of_list):
        mltples.append(int(input()))

    if is_list_mult10(mltples) == True:
        print("all multiples of 10")

    elif is_list_no_mult10(mltples) == True:
        print("no multiples of 10")

    else:
        print("mixed values")

