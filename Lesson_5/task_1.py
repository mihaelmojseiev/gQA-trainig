# 1. Write a code with all types of loops:
# Array with any data and loop that can handle it.

loop1 = ['apple', 'macbook', 'pro']

for i in loop1:
    print(i)


loop2 = 1

while loop2 < 3:
    print(loop2)
    loop2 = loop2+1


loop3 = ["apple", "macbook"]
loop3num = [1, 2]

for i in loop3:
    for o in loop3num:
        print(i,o)

if loop1 == loop3:
    print(True)
else:
    print(False)