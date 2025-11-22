print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Kiểm tra
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())
