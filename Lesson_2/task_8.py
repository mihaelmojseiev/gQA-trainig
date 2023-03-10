# 8. Create 2 variables john, marta. Variables must be dictionaries with keys: full_name, age, salary, gender, friends, coordinates.
#
# Structure requirements:
# Full_name - full name
# Age - age
# Salary - salary
# Gender - the gender of the person (use boolean)
# Friends - list of friends from task 6
# Coordinates - longitude and latitude from task 7
#
# Print the key and value for john and martha to console: “key => value” where key is the key of the dictionary pair and value is the value of the dictionary pair.
#
# + challenge
#
# Task from point 8. Instead of strings in the list of friends, there should be the same dictionaries as john and marta.
# Create 2 friends each for John and Martha. Print John and Martha's fields to the console.

sam = {
    'full_name': 'Sam Doe',
    'days left': 342234
}
rick = {
    'full_name': 'Rick Doe',
    'age': 2
}
john = {
    'full_name': 'John Doe',
    'age': 25,
    'salary': 1998,
    'gender': bool('male'),
    'friends': (sam, rick),
    'coordinates': (25.252345342,40.4565654)
}
marta = {
    'full_name': 'Marta Doe',
    'age': 26,
    'salary': 1999,
    'gender': bool(not 'male'),
    'friends': ['James', 'ter', 'Mara', 'John', 'Ma', 'John', 'John'],
    'coordinates': (26.3234523,29.457483)
}

print(john, marta)