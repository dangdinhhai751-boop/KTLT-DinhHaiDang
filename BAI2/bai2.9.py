print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
s = input("Enter a string: ")

d = {}
for ch in s:
    d[ch] = s.count(ch)

print(d)
