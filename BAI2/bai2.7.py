print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
n = int(input("Nhập vào một số nguyên n: "))

d = {}  # Tạo dictionary rỗng
for i in range(1, n + 1):
    d[i] = i * i  # Gán giá trị bình phương vào khóa i

print(d)
