print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import tkinter as tk

def handle_key_press(event):
    """
    Phương thức xử lý sự kiện khi một phím được nhấn.

    In ra ký hiệu của phím được nhấn.
    """
    key_symbol = event.keysym
    print(f"✅ Sự kiện phím bấm đã được kích hoạt: Phím '{key_symbol}' đã được nhấn.")
    
    # Bạn có thể thêm các logic khác ở đây, ví dụ:
    # if key_symbol == 'Return':
    #     print("Bạn đã nhấn phím ENTER!")

# --- Xây dựng giao diện ---

# 1. Tạo cửa sổ gốc (root window)
window = tk.Tk()
window.title("Ứng dụng Xử lý Phím bấm")
window.geometry("400x150") # Thiết lập kích thước cửa sổ

# 2. Thêm một Label hướng dẫn
label = tk.Label(window, text="Hãy nhấn bất kỳ phím nào\nđể xem kết quả trên Console/Terminal!", 
                 font=("Arial", 12))
label.pack(pady=30, padx=20)

# 3. Liên kết sự kiện Phím bấm (<Key>) với phương thức xử lý
# <Key> là một lớp sự kiện chung cho TẤT CẢ các phím bấm.
window.bind('<Key>', handle_key_press)

# Bắt đầu vòng lặp sự kiện của tkinter
print("Bắt đầu ứng dụng. Cửa sổ đã sẵn sàng nhận sự kiện phím bấm...")
window.mainloop()
print("Ứng dụng đã đóng.")
