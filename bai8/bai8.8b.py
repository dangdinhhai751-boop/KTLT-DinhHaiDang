print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import tkinter as tk
from tkinter import messagebox

def show_radio_selection(v):
    """
    Hàm xử lý sự kiện khi nút 'Click Me' được bấm.
    Lấy giá trị hiện tại của Radio Button và hiển thị thông báo.
    """
    # Lấy giá trị số nguyên hiện tại từ biến điều khiển v
    selected_value = v.get()
    
    # Tạo chuỗi thông báo
    if selected_value == 1:
        option_text = "Phương án 1"
    elif selected_value == 2:
        option_text = "Phương án 2"
    elif selected_value == 3:
        option_text = "Phương án 3"
    else:
        option_text = "Chưa có lựa chọn hợp lệ"
        
    # Hiển thị thông báo bằng hộp thoại
    messagebox.showinfo("Lựa chọn Radio Button", 
                        f"Giá trị lựa chọn hiện tại là: {selected_value}\nBạn đã chọn: {option_text}")


def create_radio_button_form():
    """
    Tạo cửa sổ Form chứa các Radio Button và nút Click Me.
    """
    # Tạo cửa sổ gốc
    form_b = tk.Tk()
    form_b.title("Form Radio Button (B)")
    form_b.geometry("300x220")
    form_b.resizable(False, False)
    
    # Biến điều khiển nhóm Radio Button
    # Biến này phải là tk.IntVar() vì giá trị của Radio Button là số nguyên (1, 2, 3)
    v = tk.IntVar()
    v.set(1) # Thiết lập giá trị mặc định là 1 (chọn Phương án 1)
    
    tk.Label(form_b, 
             text="LỰA CHỌN CỦA BẠN:", 
             font=("Arial", 12, "bold"), 
             fg="#333333").pack(pady=(20, 10))

    # --- Tạo các Radio Button ---
    
    # Radio Button 1
    tk.Radiobutton(form_b, 
                   text="Phương án 1", 
                   variable=v, 
                   value=1,
                   font=("Arial", 10)).pack(anchor=tk.W, padx=40)
                   
    # Radio Button 2
    tk.Radiobutton(form_b, 
                   text="Phương án 2", 
                   variable=v, 
                   value=2,
                   font=("Arial", 10)).pack(anchor=tk.W, padx=40)
                   
    # Radio Button 3
    tk.Radiobutton(form_b, 
                   text="Phương án 3", 
                   variable=v, 
                   value=3,
                   font=("Arial", 10)).pack(anchor=tk.W, padx=40)
    
    # --- Tạo nút "Click Me" ---
    # Sử dụng lambda để truyền biến điều khiển (v) vào hàm xử lý
    tk.Button(form_b, 
              text="Click Me", 
              command=lambda: show_radio_selection(v), 
              bg="#4CAF50", # Màu nền xanh lá cây
              fg="white", # Màu chữ trắng
              font=("Arial", 10, "bold"),
              width=15).pack(pady=20)

    # Khởi chạy vòng lặp chính
    form_b.mainloop()

# Chạy Form
if __name__ == "__main__":
    create_radio_button_form()
