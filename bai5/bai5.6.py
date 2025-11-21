print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
def tim_vi_tri_max_min(ds):
    max_val = max(ds)
    min_val = min(ds)
    vi_tri_max = ds.index(max_val)
    vi_tri_min = ds.index(min_val)
    return vi_tri_max, vi_tri_min

# Nhập danh sách
n = int(input("Nhập số phần tử: "))
ds = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ds.append(x)

vt_max, vt_min = tim_vi_tri_max_min(ds)

print("Vị trí phần tử lớn nhất:", vt_max)
print("Vị trí phần tử nhỏ nhất:", vt_min)

