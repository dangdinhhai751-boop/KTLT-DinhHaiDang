print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
def get_sum(*num):
    tmp = 0
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print("Tổng =", result)
