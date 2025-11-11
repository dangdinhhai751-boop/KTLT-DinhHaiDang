print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import math

def Tinh(R):
    if R <= 0:
        print("Bán kính không hợp lệ! Phải lớn hơn 0.")
        return
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    print("Chu vi hình tròn =", chu_vi)
    print("Diện tích hình tròn =", dien_tich)

# Nhập bán kính
R = float(input("Nhập bán kính R: "))
Tinh(R)
