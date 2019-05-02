# Desafio: Escreva uma função que tenha 3 parâmetros obrigatórios e 2 parâmetros opcionais.

def somar_numeros(x, y, z, a = 1, b = 2):
    return x + y + z + a + b

resultado = somar_numeros(5, 10, 15)

print(resultado)
