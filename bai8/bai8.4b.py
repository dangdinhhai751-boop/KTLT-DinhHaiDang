print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
from tkinter import *
# Hàm xử lý khi nút bấm được click
def clicked() :
    lbl. configure(text="Button was clicked !!")
window = Tk()
window.title ("Welcome to LikeGeeks app")
window.geometry ('350x200')
# 1. Thêm Label
lbl = Label (window, text="Hello")
lbl .grid (column=0, row=0)
# 2. Thêm Button và liên kết với hàm 'clicked'
btn = Button (window, text="Click Me", command=clicked)
btn.grid (column=1, row=0) # Đặt nút ở cột 1, hàng 0
window.mainloop ()
