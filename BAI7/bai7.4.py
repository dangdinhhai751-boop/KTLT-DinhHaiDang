print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import itertools

def read_first_n_lines(file_path, n):
    """Đọc n dòng đầu tiên của file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # itertools.islice(iterable, stop) trả về một iterator cắt từ đầu
            lines = itertools.islice(file, n)
            
            # In ra các dòng đã đọc
            print(f"Đọc {n} dòng đầu tiên từ file '{file_path}':")
            for line in lines:
                print(line.strip()) # strip() để loại bỏ ký tự xuống dòng thừa

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng:
file_path = 'D:/a.txt'
n_lines = 3  # Số dòng muốn đọc
read_first_n_lines(file_path, n_lines)
