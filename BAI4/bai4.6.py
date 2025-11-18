print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
hoten = input("Nhập họ và tên (2 từ): ").split()
if len(hoten) == 2:
    ho, ten = hoten
    print("Họ:", ho)
    print("Tên:", ten)
else:
    print("Vui lòng nhập đúng 2 từ (họ và tên riêng).")
