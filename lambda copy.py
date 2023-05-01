people = [
    {"name": "Harry", "house": "Ricardo"},
    {"name": "Draco", "house": "Dancing"},
    {"name": "Cho", "house": "Milos"},
]


people.sort(key=lambda person: person["name"])
print(people)
