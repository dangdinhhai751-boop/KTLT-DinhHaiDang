print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
n = int(input("Nhập n: "))
fibo = [0, 1]
while fibo[-1] + fibo[-2] < n:
    fibo.append(fibo[-1] + fibo[-2])
print("Dãy Fibonacci nhỏ hơn", n, "là:")
print(fibo)
