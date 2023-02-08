# 3 There is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}
import json
tias = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
pok = tias.replace(" ","").split("&")

print(pok)

