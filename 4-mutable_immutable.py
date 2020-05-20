x = 1
print(id(x))  # print address of location
# Primitive types such as int, string is immutable
x = x + 1
print(id(x))  # new reference of x because integers are immutable

x = [1, 2, 3]
print(id(x))  # notice that lists are mutable
x.append(4)
print(id(x))
