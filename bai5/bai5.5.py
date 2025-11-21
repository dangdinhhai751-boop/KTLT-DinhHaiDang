print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("--- Chương trình tìm MIN/MAX của Danh sách ---")
danh_sach = []
while True:
    try:
        so_luong = int(input("Nhập số lượng phần tử (N): "))
        if so_luong > 0:
            break
        else:
            print("Số lượng phải là số nguyên dương.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
for i in range(so_luong):
    while True:
        try:
            gia_tri = int(input(f"Nhập giá trị thứ {i + 1}: "))
            danh_sach.append(gia_tri)
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
if danh_sach:    
    max_value = max(danh_sach)
    min_value = min(danh_sach)

    print("\n--- KẾT QUẢ ---")
    print(f"Danh sách đã nhập: {danh_sach}")
    print(f"Phần tử lớn nhất (Max): {max_value}")
    print(f"Phần tử nhỏ nhất (Min): {min_value}")
else:
    print("Danh sách rỗng, không thể tìm Min/Max.")
