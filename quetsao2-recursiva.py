numero = int(input('Digite um número---> '))
def ate_zero(a, n):
    if a == -1:
        return n
    print(n)
    return ate_zero(a - 1, n + a)

ate_zero(numero - 1, numero)
