#A palindrome is a word or a phrase that is the same when read both forward and backward. 
# Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). 
# Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.



def palindrome(input_str):
    """This function identifies if a string is a palindrome"""

    # Uses list comprehension to create a normal and reversed list
    list_of_string = [x for x in input_str.split(' ')]
    list_of_string_reverse = [input_str[x] for x in reversed(range(0, len(input_str))) if input_str[x] != ' ']

    # stores values from list in string without spaces
    final_string_reversed = "".join(list_of_string_reverse)
    final_string = "".join(list_of_string)

    #compares the values
    if final_string == final_string_reversed:
        return True

    else:
        return False

if __name__ == '__main__':
    usr_string = str(input())

    if palindrome(usr_string) == True:
        print(usr_string,"is a palindrome")
    
    if palindrome(usr_string) == False:
        print(usr_string, "is not a palindrome")
