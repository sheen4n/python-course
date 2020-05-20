from pathlib import Path

path = Path("ecommerce")

print(path.iterdir())  # get all files in this path
for p in path.iterdir():
    print(p)


# List Comprehension
paths = [p for p in path.iterdir()]
print(paths)

# List Comprehension with filtering
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)


# How to search matching pattern
py_files = [p for p in path.glob("*.py")]
print(py_files)

# How to search recursively
py_files = [p for p in path.rglob("*.py")]  # use rglob
print(py_files)
