# 2 There is a list of friends ["John", "Marta", "James", "Amanda", "Marianna"].
# print to the console the names of each on a new line,
# right-aligned using the string method and formatting via f string.
# Also, above the names, in the first line, display the headings Names where
# the word names should be in the middle, and the rest of the space is filled with the symbol "*"
friends = ["John", "Marta", "James", "Amanda", "Marianna"]
headname = 'Names'

headname = headname.center(35, "*")

print(headname)

for j in range(0,len(friends)):
    print(f"{friends[j]:>20}")