print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import math

pos = [0, 0]  # Vị trí ban đầu (x=0, y=0)

print("Nhập lệnh di chuyển (ví dụ: UP 5). Nhấn Enter để dừng:")

while True:
    s = input()
    if not s:  # Dừng khi người dùng nhấn Enter trống
        break
    movement = s.split()
    direction = movement[0].upper()
    steps = int(movement[1])

    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps

distance = int(round(math.sqrt(pos[0]**2 + pos[1]**2)))
print("Khoảng cách từ vị trí ban đầu đến vị trí hiện tại là:", distance)
