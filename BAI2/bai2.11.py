print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
l = ['python', 4, 7]
k = ['rose', 2, 'guntur', 8]

# Cách 1: Gộp 2 danh sách thành danh sách con
m = []
m.append(l)
m.append(k)
print("Danh sách sau khi gộp:", m)

# Cách 2: Kết hợp thành từ điển (dictionary)
d = dict(zip(l, k))  # zip sẽ ghép các phần tử tương ứng
print("Từ điển sau khi kết hợp:", d)
