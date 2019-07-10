from math import sqrt

# Solving cubic equations
def g(x):
    return 6*x**3 + 31*x**2 + 3*x -10

def plug():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x =",x)
        x += 1
    print("done.")


# Solving quadratic equations
def quad(a,b,c):
    ''''Returns the solutions of an equation
    of the form a*x**2 + b*x + c = 0''''
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1,x2