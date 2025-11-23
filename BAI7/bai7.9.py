print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import shutil
# Hoặc sử dụng cách đọc ghi thủ công

source_file = 'source.txt' # File nguồn
destination_file = 'target.txt' # File đích

# Tạo một file nguồn giả định để sao chép
try:
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write("Đây là nội dung của file nguồn.\n")
        f.write("Nội dung này sẽ được sao chép sang file đích.")
except:
    pass # Bỏ qua nếu có lỗi tạo file

# Cách 1: Sử dụng module shutil (đơn giản nhất)
try:
    shutil.copyfile(source_file, destination_file)
    print(f"Sao chép thành công từ '{source_file}' sang '{destination_file}' (Sử dụng shutil).")

# Cách 2: Đọc và ghi thủ công
    with open(source_file, 'r', encoding='utf-8') as s_file:
        content = s_file.read()
    
    with open(destination_file + '_manual', 'w', encoding='utf-8') as d_file:
        d_file.write(content)
    
    print(f"Sao chép thành công thủ công từ '{source_file}' sang '{destination_file}_manual'.")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file nguồn '{source_file}'.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
