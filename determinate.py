import random as r

# creates random matrix filled with random numbers 1-10
def random(list):
    z = 0

    x = r.randint(2, 4)

    while len(list) <= x:
        temp = []
        y = 0

        while y <= x:
            temp.append(r.randint(0, 10))
            y += 1
        z += 1
        list.append(temp)

    return list

def zoom(list):
    new_list = []
    counter = 0

    while counter <= len(list):
        for x in range(0, len(list)):
            a = 0
            target = list[x][a]

            for y in range(0, len(list[x])):
                print(list[x][y])
        
        counter += 1


def det(m):
    counter = 0
    total = 0

    while counter <= len(m):
        pass
    
nums = []

random(nums)

for x in nums:
    print(x)

# start of "zoom in algorithm at a1"
for x in range(0, len(nums)):
    a = 0
    for y in range(0, len(nums[x])):

        if y != a and x != a:
            print(nums[x][y])
        
        

#det(nums)


