print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import tkinter as tk

# Dữ liệu cho các lựa chọn
languages = [
 ("Python", 1),
 ("Perl", 2),
 ("Java", 3),
 ("C++", 4),
 ("C", 5)
]

def ShowChoice():
    """
    Phương thức được gọi khi người dùng chọn một Indicator Button.
    In ra giá trị (value) của lựa chọn hiện tại.
    """
    print(f"✅ Lựa chọn hiện tại (Value): {v_indicator.get()}")
    
# --- Thiết lập Cửa sổ và Biến ---
root_b = tk.Tk()
root_b.title("b) Indicator Button (indicatoron=0)")

# Biến kiểm soát giá trị của nhóm Indicator Button
v_indicator = tk.IntVar()
v_indicator.set(1) # Thiết lập giá trị mặc định là 1 (Python)

# Tiêu đề
tk.Label(root_b,
         text="""Chọn ngôn ngữ (Sử dụng indicatoron=0):""",
         justify = tk.LEFT,
         padx = 20,
         font=("Arial", 10, "bold")).pack(pady=(10, 5))

# Tạo và đặt các Indicator Button
for text, val in languages:
    tk.Radiobutton(root_b,
                   text=text,
                   indicatoron = 0, # TẮT vòng tròn indicator (biến thành nút bấm)
                   width = 20,      # Đặt chiều rộng cố định cho nút
                   padx = 20,
                   pady = 5,
                   variable=v_indicator,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W) # anchor=tk.W căn lề trái

root_b.mainloop()
