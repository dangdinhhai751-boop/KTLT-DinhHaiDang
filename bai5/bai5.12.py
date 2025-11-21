print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import numpy as np

student_id     = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40.0, 42.5, 41.38, 40.0, 42.0, 45.0, 42.0])

# Sắp xếp theo chiều cao tăng dần
sorted_indices = np.argsort(student_height)

print("Sắp xếp theo chiều cao:")
print(student_id[sorted_indices])
print(student_height[sorted_indices])
# lexsort: sắp theo cột cuối trước
indices = np.lexsort((student_id, student_height))

print("Sắp xếp theo nhiều cột (height → student_id):")
print(student_id[indices])
print(student_height[indices])
