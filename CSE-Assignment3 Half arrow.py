arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))

while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))

print("")

asterisk = '*'
body = ""
head = ""


#creates arrow body
for x in range(0, arrow_base_width):
    body += asterisk

# prints arrow length
for x in range(0, arrow_base_height):
    print(body)

# creates arrow head
for x in range(0, arrow_head_width):
    head += asterisk

for x in range(arrow_head_width, 0, -1):
    print(head[:x])

