print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
file_path = 'test.txt' # Sử dụng một tên file đơn giản hơn

def append_and_display(file_path, new_content):
    """Nối nội dung mới và sau đó hiển thị toàn bộ nội dung file."""
    try:
        # 1. Nối (Append) nội dung mới vào cuối file
        print(f"Nối nội dung vào file '{file_path}'...")
        # 'a' là chế độ append, nếu file không tồn tại, nó sẽ được tạo
        with open(file_path, 'a', encoding='utf-8') as myfile:
            myfile.write(new_content)
        
        # 2. Hiển thị (Read) toàn bộ file
        print("-" * 30)
        print(f"Nội dung file '{file_path}' sau khi nối:")
        # 'r' là chế độ read
        with open(file_path, 'r', encoding='utf-8') as file_read:
            print(file_read.read())

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng:
content_to_add = "\nĐây là nội dung được thêm vào file."
append_and_display(file_path, content_to_add)
