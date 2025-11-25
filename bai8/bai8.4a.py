print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import tkinter as tk

# 1. Tạo đối tượng cửa sổ gốc (Root Window)
window = tk.Tk()

# 2. Cấu hình cửa sổ
# Đặt tiêu đề cho cửa sổ
window.title("Cửa Sổ Đồ Họa Tkinter Cơ Bản")

# Đặt kích thước mặc định cho cửa sổ (ví dụ: 400x300 pixels)
# Cú pháp: "WidthxHeight"
window.geometry("400x300")

# 3. Thêm các thành phần khác (widgets) vào đây nếu cần
# Ví dụ: Thêm một nhãn (Label)
label = tk.Label(window, text="Xin chào, đây là cửa sổ Tkinter đầu tiên của tôi!")
label.pack(pady=20) # 'pack' để sắp xếp widget và thêm khoảng đệm

# 4. Khởi chạy vòng lặp sự kiện chính (Main Event Loop)
# Đây là dòng lệnh quan trọng giúp cửa sổ hiển thị và phản hồi các sự kiện
window.mainloop()
