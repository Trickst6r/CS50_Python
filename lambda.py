# Nesting a dict inside a list
people = [
    {"name": "Harry", "house": "Ricardo"},
    {"name": "Aicardo", "house": "LoL"},
    {"name": "Milos", "house": "Dancin"},
]


# 1.  At first, an error will appear, as Python doesn't know
# how to sort those dictionaries

# 2. Defining a function (lambda) that tells the sort function
# how to do the sorting, what to look at when sorting
people.sort(key=lambda person: person["name"])


print(people)
