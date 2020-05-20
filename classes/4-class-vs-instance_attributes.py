class Point:
    default_color = "red"  # class attributes

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point - {self.x} {self.y}")


Point.default_color = "yellow"  # this affects all class level attributes

point = Point(1, 2)  # instance attributes
point.draw()
print(point.default_color)  # class level attributes
print(Point.default_color)  # class level attributes

another = Point(3, 4)  # instance attributes
another.draw()
