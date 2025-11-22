print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

# Kiểm tra
aCircle = Circle(2)
print(aCircle.area())
