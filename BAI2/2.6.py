print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
numbers = []  # Tạo danh sách rỗng để lưu kết quả

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):  # Chia hết cho 7 nhưng không chia hết cho 5
        numbers.append(str(i))  # Chuyển sang chuỗi để in sau

print(','.join(numbers))  # In ra các số, cách nhau bằng dấu phẩy
