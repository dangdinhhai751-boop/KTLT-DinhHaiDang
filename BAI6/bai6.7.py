print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius


# Kiểm tra
c = Circle(5)
print("Diện tích:", c.area())
print("Chu vi:", c.circumference())
