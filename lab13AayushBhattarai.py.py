def strip_zeros(p):
    while p and p[-1] == 0:
        p.pop()
    return p

def add_poly(p1, p2):
    size = max(len(p1), len(p2))
    p1 += [0]*(size - len(p1))
    p2 += [0]*(size - len(p2))
    return [p1[i]+p2[i] for i in range(size)]

def sub_poly(p1, p2):
    size = max(len(p1), len(p2))
    p1 += [0]*(size - len(p1))
    p2 += [0]*(size - len(p2))
    return [p1[i]-p2[i] for i in range(size)]

def mul_poly(p1, p2):
    res = [0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            res[i+j] += p1[i]*p2[j]
    return res

def div_poly(dividend, divisor):
    dividend = strip_zeros(dividend[:])
    divisor = strip_zeros(divisor[:])
    if not divisor:
        raise ZeroDivisionError("Cannot divide by zero polynomial")
    quotient = [0]*(len(dividend)-len(divisor)+1)
    while len(dividend) >= len(divisor):
        coeff = dividend[-1] // divisor[-1]
        power = len(dividend)-len(divisor)
        quotient[power] = coeff
        for i in range(len(divisor)):
            dividend[power+i] -= coeff*divisor[i]
        dividend = strip_zeros(dividend)
    remainder = dividend
    return quotient, remainder

def print_poly(p):
    if not p:
        print("0")
        return
    terms = []
    for i, coeff in enumerate(p):
        if coeff != 0:
            terms.append(f"{coeff}x^{i}" if i>0 else f"{coeff}")
    print(" + ".join(terms))

print("Enter coefficients of first polynomial :")
p1 = list(map(int, input().split()))
print("Enter coefficients of second polynomial:")
p2 = list(map(int, input().split()))

print("\nAddition:")
print_poly(add_poly(p1,p2))
print("\nSubtraction:")
print_poly(sub_poly(p1,p2))
print("\nMultiplication:")
print_poly(mul_poly(p1,p2))
print("\nDivision (Quotient and Remainder):")
try:
    q,r = div_poly(p1,p2)
    print("Quotient:", end=" "); print_poly(q)
    print("Remainder:", end=" "); print_poly(r)
except ZeroDivisionError as e:
    print(e)
