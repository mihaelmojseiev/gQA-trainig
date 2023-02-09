# 4 You have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"]
# convert it to a list of variable names for python in snake case format
# ["first_item", "friends_list", "my_tuple"]
lisq = ["FirstItem", "FriendsList", "MyTuple"]

lisq = lisq[0].lower() + lisq[1:]
for i in lisq:
    if i.isupper():
        lis = lisq.replace(i, f"_{i.lower()}")

print(lisq)
