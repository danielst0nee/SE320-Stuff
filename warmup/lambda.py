lod = [ # list of dictionaries
{"name": "George Smith", "age": 28, "married": True},
{"name": "Mary Backer", "age": 21, "married": True},
{"name": "Bill Miller", "age": 41, "married": False},
{"name": "Carol Williams", "age": 21, "married": False},
{"name": "John Doe", "age": 30, "married": False}
]

print(sorted(lod, key = lambda d: d["name"].split()[-1]))