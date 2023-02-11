# 1 You have a list of elements [1, 2, 3, 4, 5, 6, 7, 8].
# Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples where the first element is the index and the second is the value. [(index, value)].
# accordingly, elements with an even index are placed in another list of tuples with the same format as in the case with odd indices.

n = [1, 2, 3, 4, 5, 6, 7, 8]
l = len(n)
even = []
odd = []
for i in range(l):
    if i % 2 == 0:
        odd.append(n[i])
    else:
        even.append(n[i])
for index in range(len(n)):
    print('Индекс: ', index, 'Число: ', n[index])
