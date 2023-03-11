import math

def bisection_method(f, x0, x1, tol=1e-5, max_loop = 100):
    fx0 = f(x0);
    fx1 = f(x1);
    for i in range(max_loop):
        # print("----------------")
        x2 = (x0 + x1) / 2;
        fx2 = f(x2);
        print("X2::::::", x2);
        if abs(fx2) < tol:
            return x2;
        if fx2 * fx0 > 0:
            # print(f"fx2 * fx0 > 0 nen nghiem chay tu [{x2}, {x1}]")
            x0 = x2;
            fx0 = fx2;
        else:
            # print(f"fx2 * fx0 < 0 nen nghiem chay tu [{x0}, {x2}]")
            x1 = x2;
            fx1 = fx2;
def fb(x):
    return math.exp(x) - x**2 + 3*x - 2;
def fc(x):
    return 2*x*math.cos(2*x) - (x + 1) ** 2;
print(bisection_method(fc, -1, 0));
