
print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
s = input("Nhập câu: ")
chu_cai = sum(c.isalpha() for c in s)
chu_so = sum(c.isdigit() for c in s)
print("Số chữ cái là:", chu_cai)
print("Số chữ số là:", chu_so)
