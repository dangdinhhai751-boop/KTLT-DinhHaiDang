print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
def bubbleSort(nlist):
    loop = len(nlist)
    for i in range(loop-1):
        swapped = False
        for j in range(loop-i-1):
            # so sánh các phần tử cạnh nhau
            if nlist[j] > nlist[j+1]:
                # tráo đổi chúng
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True
        # Nếu không cần tráo đổi phần tử nào nữa thì
        # tức là mảng đã được sắp xếp. Thoát khỏi vòng lặp.
        if not swapped:
            break
    return nlist

# Nhập danh sách từ bàn phím
n = int(input("Nhập số lượng phần tử: "))
nlist = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(element)

# Sắp xếp danh sách
sorted_list = bubbleSort(nlist)

# In kết quả
print("Danh sách đã sắp xếp:", sorted_list)
