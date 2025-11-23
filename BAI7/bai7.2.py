print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
file_path = 'D:/a.txt' 
char_count = 0  # Biến đếm ký tự
line_count = 0  # Biến đếm dòng

try:
    with open(file_path, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line_count += 1
            char_count += len(line)

    print(f"File: {file_path}")
    print(f"Số ký tự (bao gồm khoảng trắng và ký tự xuống dòng): {char_count}")
    print(f"Số dòng: {line_count}")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file tại đường dẫn {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
