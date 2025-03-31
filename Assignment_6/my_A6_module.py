import math

def ln_taylor(z, n):
    """
    Calculate the approximation of ln(z) using the Taylor series.

    >>> round(ln_taylor(1.1, 10), 5)
    0.09531
    >>> round(ln_taylor(0.9, 10), 5)
    -0.10536
    >>> round(ln_taylor(0.8, 10), 5)
    -0.22314
    """
    result = 0.0
    for k in range(1, n+1):
        term = ((-1)**(k-1)) * ((z-1)**k) / k
        result += term
    return result

def exp_x_diff(x, z):
    """
    Evaluate the function f(x) = exp(x) - z
    This function is zero at x = ln(z).

    >>> round(exp_x_diff(0, 1), 5)
    0.0
    >>> round(exp_x_diff(1, 1), 5)
    1.71828
    >>> round(exp_x_diff(1, math.e), 5)
    0.0
    """
    return math.exp(x) - z

def ln_z_bisect(z, a0, b0, num_iter):
    """
    Calculate ln(z) using the bisection method applied to the function exp(x)-z.

    >>> round(ln_z_bisect(2.71828, 0, 2, 20), 5)
    1.0
    >>> round(ln_z_bisect(2.71828, 0, 3, 22), 5)
    1.0    
    >>> round(ln_z_bisect(2.71828, 0, 5, 24), 6)
    0.99999    
    """
    fa0 = exp_x_diff(a0, z)
    fb0 = exp_x_diff(b0, z)
    if fa0 * fb0 >= 0:
        return 'Error: The function must have different signs at a0 and b0'
    a = a0
    b = b0
    for i in range(num_iter):
        m = (a + b) / 2.0
        fm = exp_x_diff(m, z)
        if fa0 * fm < 0:
            b = m
            fb0 = fm
        else:
            a = m
            fa0 = fm
    return (a + b) / 2.0

def exp_x_diff_prime(x, z):
    """
    Evaluate the derivative of f(x) = exp(x) - z with respect to x.

    >>> round(exp_x_diff_prime(0, 1), 5)
    1.0
    >>> round(exp_x_diff_prime(1, math.e), 5)
    2.71828
    >>> round(exp_x_diff_prime(1, math.e), 7)
    2.7182818
    """
    return math.exp(x)

def ln_z_newton(z, x0, tol, num_iter):
    """
    Calculate ln(z) using Newton's method for the root of f(x) = exp(x) - z.

    >>> round(ln_z_newton(2.71828, 1, 1e-6, 20), 5)
    1.0
    >>> round(ln_z_newton(2.5, 1, 1e-6, 22), 5)
    0.91629
    >>> round(ln_z_newton(3.2, 1, 1e-6, 20), 5)
    1.16315
    """
    x = x0
    for i in range(num_iter):
        fx = exp_x_diff(x, z)
        if abs(fx) < tol:
            return x
        fpx = exp_x_diff_prime(x, z)
        if fpx == 0:
            return 'Error: Derivative zero encountered'
        x = x - fx/fpx
    return x

def exp_x_fp_fn(x, z):
    """
    Evaluate the fixed point function

    >>> round(exp_x_fp_fn(1, math.e), 5)
    1.0
    >>> round(exp_x_fp_fn(2, math.e), 5)
    -0.33539    
    >>> round(exp_x_fp_fn(1, math.e), 6)
    1.0    
    """
    return 0.5 * (z - math.exp(x) + 2*x)

def ln_z_fixed_pt(z, x0, tol, num_iter):
    """
    Calculate ln(z) using the fixed-point iteration method using the recurrence

    >>> round(ln_z_fixed_pt(2.71828, 1, 1e-6, 20), 5)
    1.0
    >>> round(ln_z_fixed_pt(2, 1, 1e-6, 25), 5)
    0.69315
    >>> round(ln_z_fixed_pt(2.75, 1, 1e-6, 15), 5)
    1.0116
    """
    x = x0
    for i in range(num_iter):
        x_next = exp_x_fp_fn(x, z)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return x


#doctest 
import doctest
doctest.testmod()
