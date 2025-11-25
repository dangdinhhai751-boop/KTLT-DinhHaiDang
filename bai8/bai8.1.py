print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import turtle

# Thiết lập cửa sổ vẽ
window = turtle.Screen()
window.bgcolor("lightgreen")

# Khởi tạo đối tượng rùa vẽ
painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)

# Định nghĩa hàm vẽ hình vuông
def drawsq(t, s):
    # Lặp 4 lần để vẽ 4 cạnh của hình vuông
    for i in range(4):
        t.forward(s) # Tiến lên s đơn vị
        t.left(90)   # Quay trái 90 độ

# Vòng lặp chính để vẽ các hình vuông xoay
# Lặp 180 lần
for i in range(1, 180):
    painter.left(18)       # Rùa quay trái 18 độ
    drawsq(painter, 200)   # Vẽ một hình vuông có cạnh dài 200 đơn vị
