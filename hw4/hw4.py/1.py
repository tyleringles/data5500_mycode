
class Rectangle:
    # maked a retangle (not a square) so I can then define it
    def __init__(self, length, width):
        self.length = length  # Assign the length passed to the object
        self.width = width    # Assign the width passed to the object

    # Finding my area by doing length times width
    def area(self):
        return self.length * self.width  # Area formula: length * width

# Create my rectangle (rember a squares a rectangle, but a rectangle isn't a square), making it with a length of 5 and a width of 3
my_rectangle = Rectangle(5, 3)

# Simply state and print the overall area of the rectangle
print("The area of the rectangle is:", my_rectangle.area())