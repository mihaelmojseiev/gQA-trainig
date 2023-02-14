# 3 There is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}
tias = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "

tias = tias.replace(' ', '').replace('&', ' ').replace('=sssss', ' ').replace('  ', ' ').replace(' ', ';')
tias = dict(tias.split("=") for tias in tias.split(";"))

print(tias)
