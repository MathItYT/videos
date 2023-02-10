from decimal import *

getcontext().prec = 100

def a_calc(n: int) -> Decimal:
    if n == 0:
        return Decimal("1")
    return (a_calc(n - 1) + b_calc(n - 1)) / 2

def b_calc(n: int) -> Decimal:
    if n == 0:
        return Decimal("0.5").sqrt()
    return (a_calc(n - 1) * b_calc(n - 1)).sqrt()

def t_calc(n: int) -> Decimal:
    if n == 0:
        return Decimal("0.25")
    return t_calc(n - 1) - p_calc(n - 1) * (a_calc(n - 1) 
                    - a_calc(n)) * (a_calc(n - 1) - a_calc(n))

def p_calc(n: int) -> Decimal:
    return Decimal(2 ** n)

def pi_calc(n: int) -> Decimal:
    return (a_calc(n) + b_calc(n)) * (a_calc(n) + b_calc(n)) / (4 * t_calc(n))

if __name__ == "__main__":
    for n in range(15):
        print(pi_calc(n))