print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
import re

value = []
items = [x for x in input("Nhập các mật khẩu, cách nhau bởi dấu phẩy: ").split(',')]

for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    if not re.search("[a-z]", p):
        continue
    elif not re.search("[0-9]", p):
        continue
    elif not re.search("[A-Z]", p):
        continue
    elif not re.search("[$#@]", p):
        continue
    else:
        value.append(p)

print(",".join(value))
Nhập các mật khẩu, cách nhau bởi dấu phẩy: ABd1234@1,a F1#,2w3E*,2We3345

