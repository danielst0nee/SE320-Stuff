names = ["Bob", "Anna", "Jim"]

k = 1
for name in names:
    print(f"{k}. {name}")
    k += 1

print()

for i, name in enumerate(names, start = 1):
    print(f"{i}. {name}")