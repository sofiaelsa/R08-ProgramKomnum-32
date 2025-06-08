# rumus Interpolasi Lagrange:
def LI(x, x_vs, y_vs):
    n = len(x_vs)
    result = 0

    for i in range(n):
        temp = y_vs[i]
        for j in range(n):
            if i != j:
                temp *= (x - x_vs[j]) / (x_vs[i] - x_vs[j])
        result += temp

    return result

# data:
x_vs = [6, 9, 12, 15]
y_vs = [234, 960, 2280, 4356]

# f(x) saat:
x = 11

# f(11):
f_x = LI(x, x_vs, y_vs)
print(f"f({x}) ≈ {f_x:.2f}")