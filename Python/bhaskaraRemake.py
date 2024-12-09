a = b = c = xm = xn = d = r = dn = 0.0

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

d = ((b*b)-(4*a*c))
print("Delta: ", d)

if d < 0:
    dn = -(b)
    d = dn
    r = d**(1/2)
    print("Raiz de delta: ", r)
    xm = ((-b + (r)) / (2*a))
    print("O valor de X1 é: ", xm, "!")
    xn = ((b - (r)) / (2*a))
    print("O valor de X2 �: ", xn, "!")
else:
    r = d**(1/2)
    print("Raiz de Delta: ", r)
    xm = ((b + (r)) / (2*a))
    print("O valor de X1 é: ", xm)
    xn = ((b - (r)) / (2*a))
    print("O valor de X2 é: ", xn)
