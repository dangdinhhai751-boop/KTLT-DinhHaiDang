print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
file_path = 'D:/a.txt' 

try:
    # Mở file ở chế độ 'r' (read)
    with open(file_path, 'r', encoding='utf-8') as file:
        # Dùng .read() để đọc toàn bộ nội dung file thành một chuỗi (string)
        content = file.read()
        
    print("Nội dung toàn bộ file:")
    print(content)

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file tại đường dẫn {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
