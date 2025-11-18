print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
ds = input("Nhập dãy từ: ").split()
max_len = max(len(tu) for tu in ds)
print("Các từ dài nhất là:")
for tu in ds:
    if len(tu) == max_len:
        print(tu)
