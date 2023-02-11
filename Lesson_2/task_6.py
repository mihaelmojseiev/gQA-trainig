# 6. Create a list with people's names, some names should be repeated in it.
# Turn a list of duplicate names into a list of unique names using sets.

friends = ['James', 'Peter', 'Marta', 'John', 'Marta', 'John', 'John']
new_friends = []

for i in friends:
    if i not in new_friends:
        new_friends.append(i)
print('Дубликаты: ', friends, '\nБез дубликатов: ', new_friends)