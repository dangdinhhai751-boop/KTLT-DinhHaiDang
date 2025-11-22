print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
class StringProcess:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.s.upper())


# Kiểm tra
sp = StringProcess()
sp.get_String()
sp.print_String()



