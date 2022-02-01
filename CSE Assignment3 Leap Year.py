# Define your function here.
def days_in_feb(year):
    """This function determines if the year is a leap year or not by seeing if the year is divisible by 4 or 4000"""

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
        return 29
    
    else:
        return 28

if __name__ == '__main__':
    # Type your code here. Your code must call the function
    user_input = int(input())

    print(user_input,"has",days_in_feb(user_input), "days in February.")