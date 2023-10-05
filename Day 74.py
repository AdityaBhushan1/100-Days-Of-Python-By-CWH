class Shape:
    def area(self):
        print("Calculating area...")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Calculating area of a circle...")
        super().area()
        return print(3.14 * self.radius * self.radius)
    

c = Circle(2)
c.area()