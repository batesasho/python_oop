class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int):
            self.radius = new_radius

    def get_area(self):
        area_of_square = Circle.pi * self.radius ** 2
        return area_of_square

    def get_circumference(self):
        circumference = 2 * Circle.pi * self.radius
        return circumference


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
