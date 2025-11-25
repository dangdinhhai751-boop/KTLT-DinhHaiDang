print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import turtle
import random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan"]

# Thiết lập cửa sổ và rùa
window = turtle.Screen()
painter = turtle.Turtle()
painter.speed(0) # Tăng tốc độ vẽ lên tối đa

num_circles = 12 # Chọn 12 vòng tròn để hình trông đầy đặn hơn
angle = 360 / num_circles # Tính góc quay đều

for i in range(num_circles):
    # Chọn màu ngẫu nhiên cho mỗi vòng tròn
    color = random.choice(colors)
    painter.pencolor(color)
    painter.pensize(2)
    
    # Vẽ vòng tròn
    painter.circle(100) 
    
    # Quay rùa một góc cố định để hình tròn tiếp theo được vẽ tại vị trí xoay
    painter.right(angle) 

turtle.done()
