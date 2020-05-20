from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")

print(ctime(path.stat().st_ctime))
print(path.read_bytes())
print(path.read_text())

path.write_text("...")
print(path.read_text())

# Copy files very verbose way, use other utility files instead
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

# target.write_text(source.read_text())  # Not recommended

#
shutil.copy(source, target)
