print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
class Hinhchunhat(object):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dientich(self):
        return self.dai * self.rong

# Kiểm tra
hcn = Hinhchunhat(5, 3)
print("Diện tích hình chữ nhật:", hcn.dientich())
