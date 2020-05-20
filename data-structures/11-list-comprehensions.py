items = [
    ("Products1", 10),
    ("Products2", 20),
    ("Products3", 30)
]

prices = list(map(lambda item: item[1], items))

# above is same as below

prices_comprehension = [item[1] for item in items]
names_comprehension = [item[0] for item in items]

print(prices)
print(prices_comprehension)
print(names_comprehension)

# we can do filtering too via list comprehension

filtered = list(filter(lambda item: item[1] >= 20, items))

# is same as this below
filtered_comprehension = [item for item in items if item[1] >= 20]

print(filtered)
print(filtered_comprehension)
