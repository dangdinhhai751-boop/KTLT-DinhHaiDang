print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
def pascal(n):
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(prev[j-1] + prev[j])
            row.append(1)
        print(row)
        prev = row

n = int(input("Nhập số dòng n: "))
pascal(n)
