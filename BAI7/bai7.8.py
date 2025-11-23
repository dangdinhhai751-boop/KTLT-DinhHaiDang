print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
file_path = 'output.txt'
data_to_write = [
    "Dòng 1: Đây là nội dung mới.",
    "Dòng 2: Nội dung này sẽ ghi đè nội dung cũ nếu file đã tồn tại.",
    "Dòng 3: Mỗi phần tử trong list sẽ là một dòng mới."
]

try:
    # 'w' là chế độ write (ghi) - tạo mới file hoặc ghi đè toàn bộ nội dung cũ
    with open(file_path, 'w', encoding='utf-8') as file:
        # Dùng writelines để ghi tất cả các chuỗi trong list
        # Cần thêm ký tự xuống dòng '\n' cho mỗi dòng
        file.writelines(item + '\n' for item in data_to_write)
        
    print(f"Đã ghi nội dung thành công vào file '{file_path}'.")

except Exception as e:
    print(f"Đã xảy ra lỗi khi ghi file: {e}")
