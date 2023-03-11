import math

def regula_falsi_method(f, x0, x1, tol=1e-6, max_loop = 100):
    fx0 = f(x0);
    fx1 = f(x1);
    for i in range(max_loop):
        x2 = x1 - ( fx1 * (x1 - x0) / (fx1 - fx0) );
        fx2 = f(x2);
        print(f"{i + 1}:::::::{x2}");
        if abs(fx2) < tol:
            return x2;
        if (fx0 * fx2) < 0:
            x1 = x2;
            fx1 = fx2;
        else:
            x0 = x2;
            fx0 = fx2;  

# [-3, -2]
# x0 = -3, x1 = -2.5
def fa(x):
    return x**3 + 3*x**2 - 1;

# [0, 3.1415/2]
# x0 = 0, x1 = 1
def fb(x):
    return x - 0.8 - 0.2* math.sin(x)

print(regula_falsi_method(fb, 0, 1));