print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import tkinter as tk
import random

# Danh sách các màu có thể
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
# BƯỚC 2: Thay đổi thời gian chơi từ 30s thành 120s
timeleft = 120 

# Biến để lưu trữ màu CẦN NHẬP (màu chữ)
target_colour = ""

def startGame(event):
    """
    Hàm bắt đầu trò chơi khi nhấn Enter.
    """
    global timeleft
    # Chỉ bắt đầu đếm ngược nếu đây là lần bắt đầu đầu tiên hoặc game đã kết thúc
    if timeleft == 120:
        # Bắt đầu bộ đếm ngược.
        countdown()
    # Chắc chắn rằng game đang chạy và có thể nhận input
    if timeleft > 0:
        nextColour()
    
# Hàm để chọn và hiển thị màu tiếp theo.
def nextColour(event=None):
    """
    Chọn ngẫu nhiên màu chữ và màu văn bản để hiển thị,
    đồng thời kiểm tra đáp án của người chơi.
    """
    global score
    global timeleft
    global target_colour

    # Nếu game đang chạy
    if timeleft > 0:
        # Đặt focus vào ô nhập liệu
        e.focus_set()
        
        # 1. KIỂM TRA ĐÁP ÁN (Chỉ kiểm tra nếu đây là sự kiện sau khi nhập/nhấn Enter)
        if event is not None and target_colour != "":
            # Lấy nội dung người chơi nhập
            input_text = e.get().lower()
            
            # Nếu màu được gõ (input_text) bằng màu chữ (target_colour)
            if input_text == target_colour.lower():
                # BƯỚC 3: Cộng 2 điểm cho lần đoán đúng
                score += 2
                print(f"✔️ Đúng! (+2 điểm). Tổng điểm: {score}")
            else:
                # BƯỚC 3: Trừ 1 điểm cho lần đoán sai
                score -= 1
                print(f"❌ Sai! (-1 điểm). Đáp án đúng là: {target_colour}. Tổng điểm: {score}")

            # Cập nhật điểm số.
            scoreLabel.config(text = "Score: " + str(score))
            
        # 2. CHUẨN BỊ MÀU MỚI
        
        # Xóa ô nhập liệu
        e.delete(0, tk.END)
        
        # Xáo trộn danh sách màu để chọn ngẫu nhiên màu chữ và màu văn bản
        random.shuffle(colours)
        
        # Chọn màu chữ ngẫu nhiên (target_colour)
        target_colour = colours[1]
        
        # Thiết lập:
        # - fg (Foreground/Màu chữ) = target_colour (Màu mà người chơi phải gõ)
        # - text (Văn bản hiển thị) = colours[0] (Màu ngẫu nhiên khác)
        label.config(fg = str(target_colour), text = str(colours[0]))
        
        
# Hàm đếm ngược thời gian
def countdown():
    """
    Thực hiện đếm ngược thời gian và cập nhật label hiển thị.
    """
    global timeleft
    
    # Nếu game vẫn đang chạy
    if timeleft > 0:
        # Giảm thời gian
        timeleft -= 1
        
        # Cập nhật label thời gian còn lại
        timeLabel.config(text = "Time left: " + str(timeleft))
        
        # Chạy lại hàm sau 1 giây (1000ms).
        root.after(1000, countdown)
    else:
        # Khi hết giờ
        label.config(text="HẾT GIỜ!", fg="red")
        e.config(state=tk.DISABLED) # Vô hiệu hóa ô nhập liệu
        scoreLabel.config(text = f"GAME OVER! Điểm cuối cùng: {score}")


# --- Driver Code (Thiết lập GUI) ---

# Tạo cửa sổ GUI
root = tk.Tk()
# Thiết lập tiêu đề
root.title("COLOR GAME - Kiểm tra tốc độ")
# Thiết lập kích thước
root.geometry("400x250")
root.resizable(False, False) # Cố định kích thước

# Thêm nhãn hướng dẫn
instructions = tk.Label(root, 
                        text = "Gõ TÊN MÀU CỦA CHỮ (không phải văn bản được hiển thị).\nNhấn ENTER để bắt đầu!",
                        font = ('Helvetica', 10), 
                        fg="darkblue")
instructions.pack(pady=10)

# Thêm nhãn điểm số
scoreLabel = tk.Label(root, text = "Điểm số: 0",
                      font = ('Helvetica', 12, 'bold'))
scoreLabel.pack(pady=5)

# Thêm nhãn thời gian còn lại
timeLabel = tk.Label(root, text = "Time left: " + str(timeleft), 
                     font = ('Helvetica', 12))
timeLabel.pack(pady=5)

# Thêm nhãn hiển thị màu sắc
label = tk.Label(root, font = ('Helvetica', 50, 'bold'))
label.pack(pady=10)

# Thêm ô nhập liệu cho người chơi
e = tk.Entry(root, width=30, justify='center', font=('Helvetica', 12))
e.pack(pady=10)

# Liên kết phím Enter (<Return>) với hàm startGame lần đầu
root.bind('<Return>', startGame) 

# Liên kết phím Enter (<Return>) với hàm nextColour sau khi game chạy để kiểm tra đáp án
# Lưu ý: Chúng ta dùng <Return> để vừa bắt đầu, vừa kiểm tra đáp án.
# Khi gọi nextColour, nó sẽ tự kiểm tra đáp án trước khi tạo màu mới.
e.bind('<Return>', nextColour)

# Bắt đầu vòng lặp GUI
root.mainloop()
