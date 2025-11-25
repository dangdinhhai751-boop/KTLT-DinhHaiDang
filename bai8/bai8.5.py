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
    Phương thức được gọi khi người dùng chọn một Radio Button.
    In ra giá trị (value) của lựa chọn hiện tại.
    """
    print(f"✅ Lựa chọn hiện tại (Value): {v.get()}")
    
# --- Thiết lập Cửa sổ và Biến ---
root_a = tk.Tk()
root_a.title("a) Radio Button Tiêu chuẩn")

# Biến kiểm soát giá trị của nhóm Radio Button
v = tk.IntVar()
v.set(1) # Thiết lập giá trị mặc định là 1 (Python)

# Tiêu đề
tk.Label(root_a,
         text="""Chọn ngôn ngữ lập trình yêu thích của bạn:""",
         justify = tk.LEFT,
         padx = 20,
         font=("Arial", 10, "bold")).pack(pady=(10, 5))

# Tạo và đặt các Radio Button
for text, val in languages:
    tk.Radiobutton(root_a,
                   text=text,
                   padx = 20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W) # anchor=tk.W căn lề trái

root_a.mainloop()
0
