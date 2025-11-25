print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import tkinter as tk

def action_click():
    """
    Hàm sẽ được gọi khi nút bấm được click.
    """
    print("Nút đã được nhấn!")

# --- Xây dựng giao diện ---

# 1. Tạo cửa sổ gốc (root window)
window = tk.Tk()
window.title("Thay đổi Màu Button")
window.geometry("350x150")

# 2. Định nghĩa các màu mong muốn
mau_nen_button = "#4CAF50"  # Mã Hex cho màu xanh lá cây đậm (để làm màu nền)
mau_chu_button = "white"    # Tên màu cho màu trắng (để làm màu chữ)

# 3. Tạo một Button và áp dụng thuộc tính 'bg' và 'fg'
button_styled = tk.Button(
    window,
    text="Nút Được Thiết Kế",
    command=action_click,
    font=("Arial", 14, "bold"),
    
    # *** THAY ĐỔI MÀU NỀN và MÀU CHỮ ***
    bg=mau_nen_button,  # Đặt màu nền (Background)
    fg=mau_chu_button   # Đặt màu chữ (Foreground)
)

# 4. Đặt Button vào cửa sổ
button_styled.pack(pady=50, padx=20)

# 5. Bắt đầu vòng lặp sự kiện của tkinter
window.mainloop()
