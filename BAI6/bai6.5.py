print("Ho va ten :Dinh Hai Dang")
print("MSSV:245752021610046")
print("---------------------")
class py_solution:
    def reverse_words(self, s):
        return " ".join(reversed(s.split()))

# Test the solution
py_sol = py_solution()
print(py_sol.reverse_words('hello .py'))  # Output: .py hello
