class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

# Example usage:
p = Point(3, -14)
print(p)  # Output: (3, -14)
