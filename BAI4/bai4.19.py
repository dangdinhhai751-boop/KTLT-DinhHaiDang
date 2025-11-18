print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
def la_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

P = tuple(i for i in range(2, 1_000_000) if la_nguyen_to(i))
print("Tuple P gồm", len(P), "số nguyên tố nhỏ hơn 1 triệu.")
