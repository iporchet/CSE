#(1) Prompt the user to enter a string of their choosing. Output the string. (1 pt) 
#(2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop in this function. (2 pts)
#(3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)
#(4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace() function in main(). (2 pts)

# 
def get_num_of_characters(input_str):
    """This function gets the total number of characters"""
    counter = 0

    for x in range(0, len(input_str)):
        counter += 1

    return counter

def output_without_whitespace(input_str):
    """This function outputs a given string with no white spaces"""
    list_of_strings = [i for i in input_str.split(' ')]
    final_string = "".join(list_of_strings)

    return final_string

if __name__ == '__main__':
    # Type your code here
    usr_inpt = str(input("Enter a sentence or phrase:"))
    print("\nYou entered:", usr_inpt, "\n")

    print("Number of characters:", get_num_of_characters(usr_inpt))

    print("String with no whitespace:", output_without_whitespace(usr_inpt))