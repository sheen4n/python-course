from datetime import datetime
import time

dt = datetime(2018, 1, 1)
dt = datetime.now()
# directives for strptime / change from string to datetime
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")

dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year} {dt.month}")

print(dt.strftime("%Y/%m"))  # change back to string
