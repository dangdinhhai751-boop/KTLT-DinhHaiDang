print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
s = input("Nhập các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")
lst = s.split(",")
ket_qua = [x for x in lst if int(x, 2) % 5 == 0]
print(",".join(ket_qua))
