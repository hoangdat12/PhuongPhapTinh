import math

def secent_method(f, x0, x1, tol=1e-5, max_loop = 100):
    for i in range(max_loop):
        fx0 = f(x0);
        fx1 = f(x1);
        x2 = x1 - (fx1 * (x1 - x0) / (fx1 - fx0));
        print(f"{i + 1}:::::{x2}");
        if abs(x2 - x1) < tol:
            return x2;
        x0 = x1;
        x1 = x2;

# [-3, -2]
# x0 = -3, x1 = -2.5
def fa(x):
    return x**3 + 3*x**2 - 1;

# [0, 3.1415/2]
# x0 = 0, x1 = 1
def fb(x):
    return x - 0.8 - 0.2* math.sin(x)

print(secent_method(fb, 0, 1));