import math

def fixed_point(f, x0 , tol = 1e-5, max_loop = 100):
    x = x0;
    for i in range(max_loop):
        x_next = f(x);
        print(f"{i + 1}::::::{x_next}");
        if abs(x_next - x) < tol:
            return x_next;
        x = x_next;
# [1,2]
# x0 = 1.5
def fa(x):
    return (2 - math.exp(x) + x**2) / 3;
def fb(x):
    return (5 / x**2) + 2;
print(fixed_point(fa, 1.5));