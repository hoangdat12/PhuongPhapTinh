import math
def newtonMethod(func, dfunc, p, tol=1e-6):
    i = 0;
    p_prev = p;
    while True:
        f = func(p_prev);
        df = dfunc(p_prev);
        p_new = p_prev - f / df;
        print(i, ": ", p_new);
        if abs(p_new - p_prev) < tol:
            return p_new;
        i+= 1;
        p_prev = p_new;

# [-3, -2]
# x0 = -2.5 || -3
def fa(x):
    return x**3 + 3*x**2 - 1;
def dfa(x):
    return 3*x**2 + 6**x;

# [0, 3.1415/2]
# x0 = 1
def fb(x):
    return x - 0.8 - 0.2* math.sin(x)
def dfb(x):
    return 1 - 0.2 * math.cos(x);
print(newtonMethod(fb, dfb, 1));

