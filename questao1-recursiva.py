x = int(input('informe um numero(Início): '))
y = int(input('informe outro numero(Fim): '))
def de_X_até_Y(x, y):
    print(x)
    x = x+1
    if x>y:
        return x
    de_X_até_Y(x, y) 
    
de_X_até_Y(x, y)

