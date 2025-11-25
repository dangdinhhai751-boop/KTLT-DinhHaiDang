print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import tkinter as tk

# --- BƯỚC 3: Định nghĩa các phương thức xử lý sự kiện ---

def NewFile():
    """Xử lý sự kiện khi chọn mục File > New."""
    print("Thông báo: Đã chọn 'New File!'")

def OpenFile():
    """Xử lý sự kiện khi chọn mục File > Open."""
    print("Thông báo: Đã chọn 'Open File!'")

def ExitApp():
    """Xử lý sự kiện khi chọn mục File > Exit."""
    print("Thông báo: Đã chọn 'Exit'. Đang đóng ứng dụng...")
    root.quit() # Sử dụng root.quit để đóng cửa sổ

def InsText():
    """Xử lý sự kiện khi chọn mục Edit > Insert Text."""
    print("Thông báo: Đã chọn 'Insert Text!'")

def InsPic():
    """Xử lý sự kiện khi chọn mục Edit > Insert Picture."""
    print("Thông báo: Đã chọn 'Insert Picture!'")

def ViewStatus():
    """Xử lý sự kiện khi chọn mục View > Status Bar."""
    print("Thông báo: Đã chọn 'Status Bar' (Chưa có hành động cụ thể).")

def About():
    """Xử lý sự kiện khi chọn mục Help > About."""
    print("Thông báo: Đây là một ví dụ đơn giản về Menu trong Tkinter.")


# --- BƯỚC 1 & 2: Tạo Window Form và Cấu trúc Menu ---

# 1. Tạo cửa sổ gốc
root = tk.Tk()
root.title("Ứng dụng với Menu Tkinter")
root.geometry("400x200")

# 2. Tạo Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar) # Liên kết Menu Bar với cửa sổ

# --- Tạo Menu "File" ---
file_menu = tk.Menu(menu_bar, tearoff=0) # tearoff=0 loại bỏ đường gạch ngang
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=NewFile)
file_menu.add_command(label="Open...", command=OpenFile)
file_menu.add_separator() # Dấu phân cách
file_menu.add_command(label="Exit", command=ExitApp)

# --- Tạo Menu "Edit" ---
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Insert Text", command=InsText)
edit_menu.add_command(label="Insert Picture", command=InsPic)

# --- Tạo Menu "View" (Sử dụng checkbutton) ---
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)

# Ví dụ về Checkbutton trong Menu
status_var = tk.IntVar()
view_menu.add_checkbutton(label="Status Bar", onvalue=1, offvalue=0, 
                          variable=status_var, command=ViewStatus)

# --- Tạo Menu "Help" ---
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="About...", command=About)

# Bắt đầu vòng lặp sự kiện của ứng dụng
root.mainloop()
