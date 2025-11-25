print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import tkinter as tk

def create_personal_info_form():
    """
    Tạo cửa sổ hiển thị thông tin cá nhân (Họ tên, Ngày sinh, MSSV, Ngành học).
    """
    # Tạo cửa sổ phụ (Toplevel) để hiển thị form
    form_info = tk.Toplevel()
    form_info.title("Thông tin Cá nhân")
    
    # Dữ liệu mẫu (Thay thế bằng thông tin thực tế của bạn)
    data = [
        ("Họ và Tên:", "ĐINH HẢI ĐĂNG"),
        ("Ngày sinh:", "07/12/2006"),
        ("MSSV:", "245752021610046"),
        ("Ngành học:", "KTDK VA TDH")
    ]
    
    # Tiêu đề Form
    tk.Label(form_info, 
             text="THÔNG TIN CÁ NHÂN", 
             font=("Arial", 14, "bold"), 
             fg="blue").grid(row=0, column=0, columnspan=2, pady=10)
    
    # Hiển thị từng mục thông tin bằng layout Grid
    for i, (label_text, value_text) in enumerate(data):
        row_num = i + 1
        
        # 1. Label cho Tên trường (Cột 0)
        tk.Label(form_info, 
                 text=label_text, 
                 font=("Arial", 10), 
                 padx=10, 
                 pady=5).grid(row=row_num, column=0, sticky=tk.W)
        
        # 2. Label cho Giá trị (Cột 1)
        # Sử dụng Anchor=tk.W để căn lề trái trong ô grid
        tk.Label(form_info, 
                 text=value_text, 
                 font=("Arial", 10, "bold"), 
                 bg="#f0f0f0", # Màu nền nhẹ cho giá trị
                 width=30, 
                 anchor=tk.W, 
                 padx=5).grid(row=row_num, column=1, sticky=tk.W + tk.E)

# --- Khởi động ứng dụng ---
# Tạo cửa sổ chính (root) để khởi chạy form
root = tk.Tk()
root.title("Bài Tập Tkinter")
root.geometry("250x100")

tk.Label(root, text="Bấm để mở Form:", font=("Arial", 12)).pack(pady=10)

# Nút mở Form Thông tin
tk.Button(root, 
          text="Mở Form Thông tin Cá nhân", 
          command=create_personal_info_form,
          bg="#add8e6").pack(pady=5)

root.mainloop()
