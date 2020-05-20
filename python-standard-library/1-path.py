from pathlib import Path

# Absolute Path
# Path("C:\\Program Files\\Microsoft")

# Raw String
# Path.(r"C:\Program Files\Microsoft") # Raw String
# Path("/usr/local/bin")
# Path() # Current Path
# Path.home
# print(Path() / "ecommerce" / "__init__.py")
path = Path("ecommerce/__init__.py")

print(path.exists())
path.is_file()
path.is_dir()

print(path.name)
print(path.stem)  # File name without extension
print(path.suffix)  # File Extension
print(path.parent)  # Folder
path = path.with_name("abc.txt")  # change the file name of pat
print(path)

print(path.absolute())  # Absolute

path = path.with_suffix(".py")  # replace suffix
print(path.absolute())
