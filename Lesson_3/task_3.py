# 3 There is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}
import ast
import json
tias = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
# tias = tias.replace('&','').split('=sssss')
tias = tias.replace(' ','').replace('&',' ').replace('=sssss',' ').replace('  ',' ').replace(' ',';')
dictionary = dict(subString.split("=") for subString in tias.split(";"))
print(dictionary)
print(tias)

#
# tias = tias.replace(' ','').split('&')
#
# while '' in tias:
#   tias.remove('')
#
# tias = [x.split('=sssss')[0] for x in tias]
# tias = strс(tias).split('=')
# stringg = ''
#
# for x in tias:
#     stringg += ' '+ x
#
# strr = stringg.replace(',', '').replace('[','').replace(']','').replace("'", '')
# print(strr)
