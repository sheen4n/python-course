from random import random, randint, choice, choices, shuffle
import string

print(random())
print(randint(1, 10))
print(choice([1, 2, 3, 4]))
print(choices([1, 2, 3, 4], k=2))
# print("".join(choices("abcdefghi", k=4)))  # password generator
print("".join(choices(string.ascii_letters, k=4)))  # password generator
print("".join(choices(string.digits, k=4)))  # password generator

numbers = [1, 2, 3, 4]
shuffle(numbers)

print(numbers)
