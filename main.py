def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b
if __name__ == "__main__":
    # Exemplo de execução manual
    print("Soma: ", soma(2, 3))
    print("Subtração: ", subtrair(5, 2))
    print("Multiplicação: ", multiplicar(3, 4))
    print("Divisão: ", dividir(10, 2))
