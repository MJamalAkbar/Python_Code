class Geometry:
    def __init__(self, length, width, radius, pi):
        self.length = length
        self.width = width
        self.radius = radius
        self.pi = pi

    def rectangle(self):
        area = self.length * self.width
        primeter = 2 * (self.length + self.width)
        print(f"Area of Rectangle = {area}")
        print(f"primeter of Rectangle = {primeter}")

    def circle(self):
        Circumferance = 2 * (self.pi * self.radius)
        Area = self.pi * self.radius * self.radius
        Diameter = 2 * self.radius
        print(f"Circumference of the circle = {Circumferance}")
        print(f"Area of the circle = {Area}")
        print(f"Area of the Diameter = {Diameter}")

    def square(self):
        perimeter = 4 * self.length
        area = self.length * self.length
        print(f"Perimeter of square = {perimeter}")
        print(f"Area of Square = {perimeter}")

object = Geometry(length=12, width=14, pi=3.14, radius=4)
object.rectangle()
object.circle()
object.square()
