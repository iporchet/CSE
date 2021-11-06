import sys
import math as m

# initialization of list
list = []
Answers = []

if len(sys.argv) > 1:
    # for loop that adds command line arguments to list[]
    for x in range(1, len(sys.argv)):
        list.append(sys.argv[x])


    # evaluates individual expressions in the list that are conjoined into one string (ie. "5+5" != "5" "+" "5")
    for x in range(0, len(list)):

        if len(list[x]) > 1:
            #kinda clunky, basically skips over expressions that can't be simplified
            try:
                list[x] = str(eval(list[x]))
                Answers.append(eval(list[x]))
                x = ''.join(list)
                
                if str(x) in str(Answers):
                    pass


            except:
                pass
        
    print(Answers)
    print(list)


else:
    pass


