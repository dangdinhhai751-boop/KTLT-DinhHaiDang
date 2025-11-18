
print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
ket_qua = []
for i in range(1000, 3001):
    if all(int(ch) % 2 == 0 for ch in str(i)):
        ket_qua.append(str(i))
print(",".join(ket_qua))
