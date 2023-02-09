# 3 There is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}
import ast
tias = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "

pok = tias.replace(' ','').split('&')

while '' in pok:
  pok.remove('')

pok = [x.split('=sssss')[0] for x in pok]
pok = str(pok).split('=')

stringg = ''
for x in pok:
    stringg += ' '+ x

print(stringg)
# keys = stringg.split(", ")
# dictionary = {}
# for i in range(len(keys)):
    # dictionary[keys[i]]
# print(dictionary)
# пока хз как доделать