class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)

# Interactive Shell
print(repr(p))  # Output: Point(x=3, y=4)  (Developer-friendly)
print(str(p))   # Output: (3, 4)          (User-friendly)
print(p)        # Output: (3, 4)          (__str__ is used here)

# If __str__ is removed
# print(p) and print(str(p)) will now output: Point(x=3, y=4)
