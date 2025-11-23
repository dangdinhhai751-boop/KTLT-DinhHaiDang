print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
def reverse_file_contents(file_path):
    """Đọc file và in nội dung của từng dòng theo thứ tự đảo ngược."""
    try:
        with open(file_path, 'r') as input_file:
            for line in input_file:
                # Dùng slicing để đảo ngược chuỗi
                reversed_line = line.rstrip('\n')[::-1]
                print(reversed_line)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đổi 'D:/a.txt' thành đường dẫn file thực tế của bạn
file_duong_dan = 'D:/a.txt' 
reverse_file_contents(file_duong_dan)
