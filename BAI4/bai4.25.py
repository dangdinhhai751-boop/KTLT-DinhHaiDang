print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
s = input("Nhập danh sách số, cách nhau bởi dấu phẩy: ")
nums = [int(x) for x in s.split(",")]
le = [str(x) for x in nums if x % 2 != 0]
print(",".join(le))
