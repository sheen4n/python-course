class Point:
    default_color = "red"  # class attributes

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point - {self.x} {self.y}")

    @classmethod  # Class Method
    def zero(cls):
        return cls(0, 0)


point = Point(0, 0)
another = Point.zero()  # class level method that returns a new object.
# Factory Method Above
