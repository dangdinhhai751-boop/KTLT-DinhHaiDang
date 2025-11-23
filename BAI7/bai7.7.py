print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
file_path = 'D:/a.txt' 
line_count = 0  # Biến đếm dòng

try:
    with open(file_path, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line_count += 1

    print(f"File: {file_path}")
    print(f"Tổng số dòng trong tệp là: {line_count}")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file tại đường dẫn {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
