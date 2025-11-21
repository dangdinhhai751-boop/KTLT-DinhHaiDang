print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")


import numpy as np

# Định nghĩa cấu trúc dữ liệu
data_type = [('name', 'S15'),
             ('class', int),
             ('height', float)]

# Danh sách sinh viên
students_details = [
    ("James", 5, 48.5),
    ("Nail", 6, 52.5),
    ("Paul", 5, 42.10),
    ("Pit", 5, 50.11)
]

# Tạo structured array
students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

print("\nSort by height:")
print(np.sort(students, order='height'))
