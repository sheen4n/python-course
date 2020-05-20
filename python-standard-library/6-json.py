import json

from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1948},
#     {"id": 2, "title": "Disney", "year": 1957},
#     {"id": 3, "title": "Wat", "year": 1923}
# ]

# data = json.dumps(movies)
# print(data)

# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0]["title"])
