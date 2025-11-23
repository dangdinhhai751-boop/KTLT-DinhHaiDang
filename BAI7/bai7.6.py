print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
def read_last_n_lines(file_path, n):
    """Đọc n dòng cuối cùng của file."""
    try:
        # Đọc tất cả các dòng vào một list
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Dùng slicing để lấy n phần tử cuối cùng của list
        # lines[-n:] sẽ trả về n phần tử cuối, hoặc tất cả nếu số dòng ít hơn n
        last_n_lines = lines[-n:]
        
        print(f"Đọc {n} dòng cuối cùng từ file '{file_path}':")
        for line in last_n_lines:
            print(line.strip()) # strip() để loại bỏ ký tự xuống dòng thừa

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng:
file_path = 'D:/a.txt'
n_lines = 2 # Số dòng muốn đọc
read_last_n_lines(file_path, n_lines)

