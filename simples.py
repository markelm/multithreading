import sympy

def resolve_simples(data):
    tamanholista = len(data)
    #primos = []
    primos = 0
    for i in range(tamanholista):
        if sympy.isprime(data[i]):
            #primos.append(data[i])
            primos += 1
    return primos