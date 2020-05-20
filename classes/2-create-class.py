class Point:
    def draw(self):
        print("draw")


pointObject = Point()
print(type(pointObject))
print(isinstance(pointObject, int))  # Check Type
pointObject.draw()
