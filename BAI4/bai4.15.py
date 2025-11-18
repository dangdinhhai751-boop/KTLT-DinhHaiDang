print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
s = input("Nhập các từ tiếng Anh, cách nhau bởi dấu cách: ")
words = s.split()  # tách thành list từ
words.sort()       # sắp xếp theo thứ tự từ điển
print("Các từ theo thứ tự từ điển là:")
for w in words:
    print(w)
