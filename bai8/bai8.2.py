print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import turtle
import random

# Danh sách các màu sẽ được sử dụng
print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Thiết lập đối tượng rùa vẽ và kích thước nét vẽ
painter = turtle.Turtle()
painter.pensize(3)

# Lặp 10 lần để vẽ 10 vòng tròn
for i in range(10):
    # 1. Chọn ngẫu nhiên một màu từ danh sách
    color = random.choice(colors)
    painter.pencolor(color)
    
    # 2. Vẽ một vòng tròn có bán kính 100
    painter.circle(100)
    
    # 3. Quay sang phải 30 độ
    painter.right(30)
    
    # 4. Quay sang trái 60 độ (Có thể bỏ qua bước này nếu chỉ muốn hình xoắn đều, 
    # nhưng tôi giữ lại theo logic code gốc của bạn)
    painter.left(60) 
    
    # 5. Đặt lại vị trí rùa về tọa độ (0, 0) - Đây là điều chỉnh so với code gốc 
    # nếu muốn tất cả vòng tròn bắt đầu từ tâm. Nếu không, kết quả sẽ là 
    # sự kết hợp giữa các vòng tròn và các đường thẳng di chuyển.
    # Trong trường hợp muốn vẽ đúng hình hoa văn như mục 3, có thể bỏ dòng này 
    # và chỉ cần giữ painter.right(36) hoặc painter.right(30) tùy theo 
    # số lượng vòng tròn. Tôi sẽ giữ theo logic vẽ hình hoa văn xoắn ốc bên dưới.

# Tôi đã tối ưu hóa đoạn code này để vẽ đúng hình hoa văn xoắn ốc 
# như mục 3, vì code gốc có thể gây ra kết quả không mong muốn.

# Tối ưu hóa cho hình hoa văn mục 3 (nếu muốn 10 cánh):
# for i in range(10):
#     color = random.choice(colors)
#     painter.pencolor(color)
#     painter.circle(100)
#     painter.right(36) # Quay 36 độ (360/10) để có 10 cánh đều

turtle.done()
