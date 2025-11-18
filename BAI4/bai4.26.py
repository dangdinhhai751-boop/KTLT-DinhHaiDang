print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
tong = 0
while True:
    s = input("Nhập giao dịch (D/W SỐ_TIỀN), hoặc Enter để dừng: ")
    if not s:
        break
    loai, so = s.split()
    so = int(so)
    if loai.upper() == 'D':
        tong += so
    elif loai.upper() == 'W':
        tong -= so

print("Số tiền thực của tài khoản là:", tong)
